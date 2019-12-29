from antlr4 import *

from lex.gen.clipslexer import clipslexer
from lex.gen.clipsparser import clipsparser
from lex.gen.clipsparserListener import clipsparserListener
from lex.gen.clips2drools_match import Drl_Match
import os
import pickle
import json


# 此文件用于将clips规则中病人指标的替换为北肿医院数据指标

def main():
    full_filename = []  # 存放所有clp完整文件名
    filename = []  # 仅存放所有clp文件名，不包括后缀
    # member_variable = {}#存放Patient所有成员变量
    mis = {}
    path = 'F:/规则语言/clips/rule3/'
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.clp'):
                full_filename.append(os.path.join(root, file))
                filename.append(os.path.splitext(file)[0])
    i = 1
    for name in full_filename:
        print('正在翻译第%s个文件...' % i)
        f = FileStream(name, 'ansi', 'strict')  # 输入文件
        lexer = clipslexer(f)  # 词法分析
        tokens = CommonTokenStream(lexer)
        parser = clipsparser(tokens)  # 语法分析
        a = parser.prog()  # 语法分析树
        listener = Drl_Match(filename[i - 1])  # 自定义语法监听器
        walker = ParseTreeWalker()
        walker.walk(listener, a)  # 遍历语法树

        str = 'package kbs\n\n'
        str += 'import java.util.ArrayList;\n'
        str += 'import cdss.kb.DataNotice_Result;\n'
        str += 'import cdss.kb.Deffunction;\n\n'
        str += 'import cdss.kb.core.engineInputModel.Patient;\n'
        str += 'import cdss.kb.core.engineInputModel.PatientInfo;\n'
        str += 'import cdss.kb.core.engineInputModel.LabTestResult;\n'
        str += 'import cdss.kb.core.engineInputModel.PhysicalSign;\n'
        str += 'import cdss.kb.core.engineInputModel.PastHistory;\n'
        str += 'import cdss.kb.core.engineInputModel.FamilyHistory;\n'
        str += 'import cdss.kb.core.engineInputModel.Diagnosis;\n'
        str += 'import cdss.kb.core.engineInputModel.Order;\n'
        str += 'import cdss.kb.core.engineOutputModel.Task;\n'
        str += 'import cdss.kb.core.engineOutputModel.Description;\n'
        str += 'import cdss.kb.core.engineOutputModel.FormatText;\n'
        str += 'import cdss.kb.core.engineOutputModel.MDTModel;\n'
        str += 'import cdss.kb.core.engineOutputModel.Process;\n'
        str += 'import cdss.kb.core.engineOutputModel.Problem;\n'
        str += 'import cdss.kb.core.engineOutputModel.Scenario;\n\n\n'

        str += listener.getDRL(a)  # 翻译后内容
        # member_variable.update(listener.variable)
        mis.update(listener.mis_var)
        output = 'F:/java_project/drl_test/src/main/resources/beizhong_rules/' + filename[i - 1] + '.drl'
        new_drl_file = open(output, 'w', encoding="utf-8")
        new_drl_file.write(str)  # 写入新文件
        new_drl_file.close()
        i = i + 1
    # # 保存所有变量
    # var_save = open('entrance_variable.txt','w')
    # en_json = json.dumps(member_variable)
    print(mis)
    # var_save.write(en_json)
    # var_save.close()
    var_save = open('mis_variable.txt', 'w')
    en_json = json.dumps(mis)
    var_save.write(en_json)
    var_save.close()


if __name__ == '__main__':
    main()
