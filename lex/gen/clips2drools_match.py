# 监视器
# 将获得的clips语法转换为drools语法
from antlr4 import *
from lex.gen.clipsparserListener import clipsparserListener
from lex.gen.clipsparser import clipsparser
import json


class Drl_Match(clipsparserListener):
    # 存放defrule或deffunction结构中出现的变量
    var_name_list = []
    # 记录当前进入的结构
    construct = ''
    # 存放自定义函数名及返回值类型
    deffunction = {'Leaf': 'String', 'Transform': 'boolean', 'Check': 'boolean', 'NotifyOrNot': 'boolean',
                   'AddOrNot': 'String', 'DataShortJudge': 'boolean', 'FourInFiveOut': 'double',
                   'ConfirmGlucoseLevel': 'void',
                   'Recommendation': 'void', 'InterpretationIndex': 'void', 'FactUsed': 'void',
                   'FileLoadNotify': 'void', 'DataNotify': 'void', 'FamilyHis': 'double',
                   'His': 'double'}
    # 存放clp文件中出现的各种类型变量
    double_var = []
    string_var = []
    boolean_var = []
    variable = {}
    patient_variable = {}  # 存放导入patient类所有成员变量及其数据类型
    beizhong_variable = {}  # 存放北肿数据类型
    last_filename = ''  # 存放当前翻译文件名
    current_filename = ''  # 存放load函数内文件名
    filename = ''  # 存放当前翻译文件名
    load = 0  # 判断是否存在load函数
    data_model = {}  # 存放用于修改的数据模型
    mis_var = {}  # 存放丢失变量
    description = 0  # 判断当前文件是否存在Recommendation 0：不存在， 1：存在
    formatText_number = 0  # 当前文件formatText个数
    NotifyOrNot = 0  # 判断当前文件是否存在NotifyOrNot 0：不存在， 1：存在
    Recommendation = 0  # 判断当前文件是否存在Recommendation 0：不存在， 1：存在
    convert_string = ''  # 用于存放强制类型转换语句
    deffunc_name = ''  # 存放当前自定义函数名
    history = 0  # 检测是否有病史数据出现 0:出现 1：不出现
    drool = 0  # 判断当前文件是否为终点 1:是 0: 不是

    def __init__(self, filename: str):
        self.drools = {}
        self.double_var = []
        self.string_var = []
        self.boolean_var = []
        self.variable = {}
        self.beizhong_variable = {}
        self.load = 0
        # 存放defrule或deffunction结构中出现的变量
        self.var_name_list = []
        # 记录当前进入的结构
        self.construct = ''
        # 存放当前翻译文件名
        self.filename = filename
        self.current_filename = ''
        self.last_filename = ''
        # 导入导入patient类所有成员变量及其数据类型
        r = open('variable.txt', 'r')
        dict_new = r.read()
        r.close()
        self.patient_variable = json.loads(dict_new)

        # 2019.12.18更新
        r = open('entrance_variable_class.txt', 'r')
        dict_new = r.read()
        r.close()
        self.data_model = json.loads(dict_new)

        # 北肿数据模型
        r = open('beizhong_variable.txt', 'r', encoding='utf-8')
        dict_new = r.read()
        r.close()
        self.beizhong_variable = json.loads(dict_new)

        self.mis_var = {}
        self.description = 0
        self.formatText_number = 0
        self.NotifyOrNot = 0
        self.Recommendation = 0
        self.convert_string = ''
        self.deffunc_name = ''
        self.history = 0
        self.drool = 0

    def getDRL(self, ctx):
        return self.drools[ctx]

    def setDRL(self, ctx, value):
        self.drools[ctx] = value

    def setrule(self, lhs, rhs, rule_name):
        # drools规则模板

        lhs += '$r : DataNotice_Result()\n'  # 诊断结果
        lhs += '$f : Deffunction()\n'  # 自定义函数Leaf
        lhs += '$MDTModel : MDTModel()'
        # 变量声明部分
        declare = ''
        if len(self.double_var) != 0:
            declare += 'double '
            for var in self.double_var:
                if self.double_var.index(var) == len(self.double_var) - 1:
                    declare += '%s=0' % var
                else:
                    declare += '%s=0,' % var
            declare += ';\n'
        if len(self.string_var) != 0:
            declare += 'String '
            for var in self.string_var:
                if self.string_var.index(var) == len(self.string_var) - 1:
                    declare += '%s' % var
                else:
                    declare += '%s,' % var
            declare += ';\n'
        if len(self.boolean_var) != 0:
            declare += 'boolean '
            for var in self.boolean_var:
                if self.boolean_var.index(var) == len(self.boolean_var) - 1:
                    declare += '%s' % var
                else:
                    declare += '%s,' % var
            declare += ';\n'
        # 变量强制类型转换
        rhs = self.convert_string + declare + rhs
        # 按格式缩进lhs及rhs部分
        temp = []
        new = ''
        temp = lhs.splitlines(True)
        i = 0
        while i < len(temp):
            temp[i] = '\t\t' + temp[i]
            new += temp[i]
            i = i + 1
        lhs = new
        new = ''
        temp = rhs.splitlines(True)
        i = 0
        while i < len(temp):
            temp[i] = '\t\t' + temp[i]
            new += temp[i]
            i = i + 1
        rhs = new
        buf = ''
        buf += 'rule "%s"\n' % rule_name
        buf += '\tlock-on-active true\n'
        buf += '\tagenda-group "%s"\n' % self.filename
        buf += '\twhen\n'
        if lhs == '':
            buf += '%s' % lhs
        else:
            buf += '%s\n' % lhs
        buf += '\tthen\n'

        if rhs == '':
            buf += '%s' % rhs
        else:
            buf += '%s\n' % rhs
        if self.Recommendation > 0:
            if self.formatText_number > 0:
                buf += '\t\tDescription $description = new Description();\n'
                for i in range(self.formatText_number):
                    buf += '\t\t$description.addFormatText( $formatText%s );\n' % (i + 1)
                buf += '\t\tTask $task = new Task();\n'
                buf += '\t\t$task.setDescription( $description );\n'
                if ('MS_DM' or 'MS_MS_mergexml') in self.filename:
                    if self.drool != 1:
                        buf += '\t\tFormatText $formatText_expl = new FormatText();\n'
                        buf += '\t\t$formatText_expl.setValue( "血糖 " + $Patient.getLabTestResult(' \
                               '"FBG_Variable").getResult() + " " + $Patient.getLabTestResult(' \
                               '"FBG_Variable").getUnit() ' \
                               ');\n '
                        buf += '\t\tDescription expl = new Description();\n'
                        buf += '\t\texpl.addFormatText($formatText_expl);\n'
                        buf += '\t\tArrayList<Description> EXPL = new ArrayList<>();\n'
                        buf += '\t\tEXPL.add(expl);\n'
                        buf += '\t\t$task.setExplanation(EXPL);\n'
                    buf += '\t\t$scenario.getProblem("糖尿病诊断").addTask($task);\n'

                elif 'MS_Hypertension' in self.filename:
                    if self.drool != 1:
                        buf += '\t\tFormatText $formatText_explanation = new FormatText();\n'
                        buf += '\t\t$formatText_explanation.setValue( "血压 " + $Patient.getLabTestResult(' \
                               '"DBP_Top_Variable").getResult() + "-" + $Patient.getLabTestResult(' \
                               '"SBP_Top_Variable").getResult() ' \
                               ');\n '
                        buf += '\t\tDescription explanation = new Description();\n'
                        buf += '\t\texplanation.addFormatText($formatText_explanation);\n'
                        buf += '\t\tArrayList<Description> explanationList = new ArrayList<>();\n'
                        buf += '\t\texplanationList.add(explanation);\n'
                        buf += '\t\t$task.setExplanation(explanationList);\n'
                    buf += '\t\t$scenario.getProblem("高血压诊断").addTask($task);\n'
                elif 'MS_Dyslipidemia' in self.filename:
                    if self.drool != 1:
                        buf += '\t\tFormatText $formatText_explanation1 = new FormatText();\n'
                        buf += '\t\t$formatText_explanation1.setValue( "总胆固醇 " + $Patient.getLabTestResult(' \
                               '"TC_Variable").getResult() + " " + $Patient.getLabTestResult("TC_Variable").getUnit() ' \
                               ');\n '
                        buf += '\t\tFormatText $formatText_explanation2 = new FormatText();\n'
                        buf += '\t\t$formatText_explanation2.setValue( "甘油三脂 " + $Patient.getLabTestResult(' \
                               '"TG_Variable").getResult() + "-" + $Patient.getLabTestResult("TG_Variable").getUnit() ' \
                               ');\n '
                        buf += '\t\tFormatText $formatText_explanation3 = new FormatText();\n'
                        buf += '\t\t$formatText_explanation2.setValue( "HDL-C " + $Patient.getLabTestResult(' \
                               '"HDLch_Variable").getResult() + "-" + $Patient.getLabTestResult(' \
                               '"HDLch_Variable").getUnit() ' \
                               ');\n '
                        buf += '\t\tFormatText $formatText_explanation4 = new FormatText();\n'
                        buf += '\t\t$formatText_explanation2.setValue( "LDL-C " + $Patient.getLabTestResult(' \
                               '"LDLch_Variable").getResult() + "-" + $Patient.getLabTestResult("LDLch_Variable").getUnit() ' \
                               ');\n '
                        buf += '\t\tDescription explanation = new Description();\n'
                        buf += '\t\texplanation.addFormatText($formatText_explanation1);\n'
                        buf += '\t\texplanation.addFormatText($formatText_explanation2);\n'
                        buf += '\t\texplanation.addFormatText($formatText_explanation3);\n'
                        buf += '\t\texplanation.addFormatText($formatText_explanation4);\n'
                        buf += '\t\tArrayList<Description> explanationList = new ArrayList<>();\n'
                        buf += '\t\texplanationList.add(explanation);\n'
                        buf += '\t\t$task.setExplanation(explanationList);\n'
                    buf += '\t\t$scenario.getProblem("血脂紊乱诊断").addTask($task);\n'
        buf += 'end\n\n'
        return buf

    def exitIf_then_else(self, ctx: clipsparser.If_then_elseContext):
        # if后条件表达式
        expr1 = self.getDRL(ctx.expression())
        action1 = action2 = ''
        # then后表达式
        if (ctx.ELSE() == None):
            for pctx in ctx.action():
                temp2 = '%s' % self.getDRL(pctx)  # then后表达式
                if temp2 != '':
                    action1 += '%s\n' % temp2
            # 按格式缩进then后action1
            temp = []
            new = ''
            temp = action1.splitlines(True)
            z = 0
            while z < len(temp):
                temp[z] = '\t' + temp[z]
                new += temp[z]
                z = z + 1
            action1 = new
        else:
            i = 0
            add_then = 0
            add_else = 0
            for child in ctx.getChildren():
                if child == ctx.THEN():
                    add_then = i
                if child == ctx.ELSE():
                    add_else = i
                i += 1
            j = ctx.getChildCount() - 1
            i = 0
            for child in ctx.getChildren():
                if i > add_then and i < add_else:
                    temp3 = '%s' % self.getDRL(child)  # then后表达式
                    if temp3 != '':
                        action1 += '%s\n' % self.getDRL(child)  # then后表达式
                if i > add_else and i < j:
                    temp3 = '%s' % self.getDRL(child)  # then后表达式
                    if temp3 != '':
                        action2 += '%s\n' % self.getDRL(child)  # else后表达式
                i = i + 1
            # 按格式缩进else后action2
            temp = []
            new = ''
            temp = action1.splitlines(True)
            z = 0
            while z < len(temp):
                temp[z] = '\t' + temp[z]
                new += temp[z]
                z = z + 1
            action1 = new
            # 按格式缩进else后action2
            temp = []
            new = ''
            temp = action2.splitlines(True)
            z = 0
            while z < len(temp):
                temp[z] = '\t' + temp[z]
                new += temp[z]
                z = z + 1
            action2 = new
        # 注释翻译
        if ctx.COMMENT() != None:
            comment = ''
            for pctx in ctx.COMMENT():
                comment += '//%s\n' % pctx.getText()[1:-2]
            buf = '%s' % comment
            buf += 'if (%s) {\n' % expr1
        else:
            buf = 'if (%s) {\n' % expr1
        buf += '%s' % action1
        # 用于判断recommendation是否在if_then结构中
        if self.NotifyOrNot == 1 and self.construct == 'defrule':
            if self.formatText_number > 0:
                if ('MS_DM' or 'MS_MS_mergexml') in self.filename:
                    buf += '\tDescription $description = new Description();\n'
                    # buf += '\tif($scenario.getProblem("糖尿病诊断").getTasks().size() != 0){\n'
                    buf += '\tif ($MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                           '"入院筛查").getTaskById("糖尿病")!=null){\n '
                    for i in range(self.formatText_number):
                        buf += '\t\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                               '"入院筛查").getTaskById("糖尿病").getDescription().addFormatText($formatText%s);\n' % (
                                       i + 1)
                    buf += '\t}else {\n'
                    buf += '\t\tFormatText $stable_formatText = new FormatText();\n'
                    buf += '\t\t$stable_formatText.setValue("糖尿病");\n'
                    buf += '\t\t$stable_formatText.setType(2);\n'
                    buf += '\t\t$description.addFormatText($stable_formatText);\n'
                    for i in range(self.formatText_number):
                        buf += '\t\t$description.addFormatText( $formatText%s );\n' % (i + 1)
                    buf += '\t\tTask $Task = new Task();\n'
                    buf += '\t\t$Task.setDescription( $description );\n'
                    buf += '\t\t$Task.setTaskID("糖尿病");\n'
                    buf += '\t\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem("入院筛查").addTask(' \
                           '$Task);\n '
                    buf += '\t}\n'
                    if self.drool != 1:
                        buf += '\tFormatText $formatText_explanation = new FormatText();\n'
                        buf += '\t$formatText_explanation.setValue( "血糖 " + $Patient.getLabTestResult(' \
                               '"%s").getResult() + " " + $Patient.getLabTestResult(' \
                               '"%s").getUnit());\n ' % (
                                   self.beizhong_variable["FBG_Variable"], self.beizhong_variable["FBG_Variable"])
                        buf += '\t$formatText_explanation.setType(8);\n'
                        buf += '\tDescription explanation = new Description();\n'
                        buf += '\texplanation.addFormatText($formatText_explanation);\n'
                        buf += '\tArrayList<Description> explanationList = new ArrayList<>();\n'
                        buf += '\texplanationList.add(explanation);\n'
                        buf += '\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                               '"入院筛查").getTaskById("糖尿病").setExplanation(explanationList);\n '
                elif 'MS_Hypertension' in self.filename:
                    buf += '\tDescription $description = new Description();\n'
                    # buf += '\tif($scenario.getProblem("糖尿病诊断").getTasks().size() != 0){\n'
                    buf += '\tif ($MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                           '"入院筛查").getTaskById("高血压")!=null){\n '
                    for i in range(self.formatText_number):
                        buf += '\t\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                               '"入院筛查").getTaskById("高血压").getDescription().addFormatText($formatText%s);\n' % (
                                       i + 1)
                    buf += '\t}else {\n'
                    buf += '\t\tFormatText $stable_formatText = new FormatText();\n'
                    buf += '\t\t$stable_formatText.setValue("高血压");\n'
                    buf += '\t\t$stable_formatText.setType(2);\n'
                    buf += '\t\t$description.addFormatText($stable_formatText);\n'
                    for i in range(self.formatText_number):
                        buf += '\t\t$description.addFormatText( $formatText%s );\n' % (i + 1)
                    buf += '\t\tTask $Task = new Task();\n'
                    buf += '\t\t$Task.setDescription( $description );\n'
                    buf += '\t\t$Task.setTaskID("高血压");\n'
                    buf += '\t\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem("入院筛查").addTask(' \
                           '$Task);\n '
                    buf += '\t}\n'
                    if self.drool != 1:
                        buf += '\tFormatText $formatText_explanation = new FormatText();\n'
                        if "DBP_Top_Variable" in self.beizhong_variable:
                            buf += '\t$formatText_explanation.setValue( "血压 " + $Patient.getLabTestResult(' \
                                   '"%s").getResult() + "-" + $Patient.getLabTestResult("%s").getResult());\n ' % (
                                       self.beizhong_variable["DBP_Top_Variable"],
                                       self.beizhong_variable["SBP_Top_Variable"])
                        else:
                            buf += '\t$formatText_explanation.setValue( "血压 " + $Patient.getLabTestResult(' \
                                   '"DBP_Top_Variable").getResult() + "-" + $Patient.getLabTestResult(' \
                                   '"SBP_Top_Variable").getResult());\n'
                        buf += '\t$formatText_explanation.setType(8);\n'
                        buf += '\tDescription explanation = new Description();\n'
                        buf += '\texplanation.addFormatText($formatText_explanation);\n'
                        buf += '\tArrayList<Description> explanationList = new ArrayList<>();\n'
                        buf += '\texplanationList.add(explanation);\n'
                        buf += '\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                               '"入院筛查").getTaskById("高血压").setExplanation(explanationList);\n '
                elif 'MS_Dyslipidemia' in self.filename:
                    buf += '\tDescription $description = new Description();\n'
                    # buf += '\tif($scenario.getProblem("糖尿病诊断").getTasks().size() != 0){\n'
                    buf += '\tif ($MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                           '"入院筛查").getTaskById("血脂紊乱")!=null){\n '
                    for i in range(self.formatText_number):
                        buf += '\t\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                               '"入院筛查").getTaskById("血脂紊乱").getDescription().addFormatText($formatText%s);\n' % (
                                       i + 1)
                    buf += '\t}else {\n'
                    buf += '\t\tFormatText $stable_formatText = new FormatText();\n'
                    buf += '\t\t$stable_formatText.setValue("血脂紊乱");\n'
                    buf += '\t\t$stable_formatText.setType(2);\n'
                    buf += '\t\t$description.addFormatText($stable_formatText);\n'
                    for i in range(self.formatText_number):
                        buf += '\t\t$description.addFormatText( $formatText%s );\n' % (i + 1)
                    buf += '\t\tTask $Task = new Task();\n'
                    buf += '\t\t$Task.setDescription( $description );\n'
                    buf += '\t\t$Task.setTaskID("血脂紊乱");\n'
                    buf += '\t\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem("入院筛查").addTask(' \
                           '$Task);\n '
                    buf += '\t}\n'
                    if self.drool != 1:
                        buf += '\tFormatText $formatText_explanation1 = new FormatText();\n'
                        buf += '\t$formatText_explanation1.setValue( "总胆固醇 " + $Patient.getLabTestResult(' \
                               '"%s").getResult() + " " + $Patient.getLabTestResult("%s").getUnit() ' \
                               ');\n ' % (self.beizhong_variable["TC_Variable"], self.beizhong_variable["TC_Variable"])
                        buf += '\t$formatText_explanation1.setType(8);\n'
                        buf += '\tFormatText $formatText_explanation2 = new FormatText();\n'
                        buf += '\t$formatText_explanation2.setValue( "甘油三脂 " + $Patient.getLabTestResult(' \
                               '"%s").getResult() + "-" + $Patient.getLabTestResult("%s").getUnit() ' \
                               ');\n ' % (self.beizhong_variable["TG_Variable"], self.beizhong_variable["TG_Variable"])
                        buf += '\t$formatText_explanation2.setType(8);\n'
                        buf += '\tFormatText $formatText_explanation3 = new FormatText();\n'
                        buf += '\t$formatText_explanation3.setValue( "HDL-C " + $Patient.getLabTestResult(' \
                               '"%s").getResult() + "-" + $Patient.getLabTestResult("%s").getUnit() ' \
                               ');\n ' % (
                                   self.beizhong_variable["HDLch_Variable"], self.beizhong_variable["HDLch_Variable"])
                        buf += '\t$formatText_explanation3.setType(8);\n'
                        buf += '\tFormatText $formatText_explanation4 = new FormatText();\n'
                        buf += '\t$formatText_explanation4.setValue( "LDL-C " + $Patient.getLabTestResult(' \
                               '"%s").getResult() + "-" + $Patient.getLabTestResult("%s").getUnit() ' \
                               ');\n ' % (
                                   self.beizhong_variable["LDLch_Variable"], self.beizhong_variable["LDLch_Variable"])
                        buf += '\t$formatText_explanation4.setType(8);\n'
                        buf += '\tDescription explanation = new Description();\n'
                        buf += '\texplanation.addFormatText($formatText_explanation1);\n'
                        buf += '\texplanation.addFormatText($formatText_explanation2);\n'
                        buf += '\texplanation.addFormatText($formatText_explanation3);\n'
                        buf += '\texplanation.addFormatText($formatText_explanation4);\n'
                        buf += '\tArrayList<Description> explanationList = new ArrayList<>();\n'
                        buf += '\texplanationList.add(explanation);\n'
                        buf += '\t$MDTModel.getProcess("北肿诊断").getScenario("肿瘤多学科门诊决策").getProblem(' \
                               '"入院筛查").getTaskById("血脂紊乱").setExplanation(explanationList);\n '
                self.Recommendation = 0
        buf += '}'
        if (ctx.ELSE() != None):
            buf += 'else {\n'
            buf += '%s' % action2
            buf += '}'
        self.setDRL(ctx, buf)
        self.NotifyOrNot = 0
        self.Recommendation = 0

    def exitDefrule(self, ctx: clipsparser.DefruleContext):
        rule_name = self.getDRL(ctx.rule_name())
        lhs = ''  # 规则lhs部分
        lhs1 = ''
        lhs2 = ''
        rhs = ''  # 规则rhs部分
        num = 0
        exists = []

        # 判断conditioal_element个数
        for pctx1 in ctx.conditional_element():
            if pctx1.getChild(0).getRuleIndex() == 61:
                temp = self.getDRL(pctx1)
                if temp != '':
                    num = num + 1
                    if '\n' in temp:
                        temp = temp.split('\n')
                        if len(temp) > 2:
                            for t in temp[1:]:
                                if t not in exists:
                                    exists.append(t)
                                    lhs2 += t
                                    if temp.index(t) != len(temp) - 1:
                                        lhs2 += '\n'
                        else:
                            exists.append(temp[1])
                            lhs2 += temp[1]
                        if lhs2 != '':
                            lhs2 += '\n'
                        if temp[0] not in exists:
                            exists.append(temp[0])
                            if num == 1:
                                lhs1 += temp[0]
                            else:
                                lhs1 += ', '
                                lhs1 += temp[0]
                    else:
                        if num == 1:
                            lhs1 += self.getDRL(pctx1)
                        else:
                            lhs1 += ', '
                            lhs1 += self.getDRL(pctx1)
        lhs1 = '$Patient : Patient( %s )\n' % lhs1
        lhs = lhs1 + lhs2
        # 判断action个数
        for pctx2 in ctx.action():
            rhs += ('%s' % self.getDRL(pctx2))
            if self.getDRL(pctx2) != '' and ctx.action().index(pctx2) != len(ctx.action()) - 1:
                rhs += '\n'
        buf = self.setrule(lhs, rhs, rule_name)
        self.setDRL(ctx, buf)
        self.construct = ''
        self.var_name_list = []
        self.double_var = []
        self.string_var = []
        self.boolean_var = []
        self.variable = {}
        self.load = 0
        self.Recommendation = 0
        self.NotifyOrNot = 0
        self.formatText_number = 0
        self.convert_string = ''
        self.history = 0
        self.drool = 0

    def exitDeffunction(self, ctx: clipsparser.DeffunctionContext):
        function_name = self.getDRL(ctx.symbol_expression())
        parameter = self.getDRL(ctx.parameter())
        action = []
        # 存放action
        for pctx in ctx.action():
            action.append(self.getDRL(pctx))
        buf_action = ''
        if len(self.double_var) != 0:
            buf_action += 'double '
            for var in self.double_var:
                if self.double_var.index(var) == len(self.double_var) - 1:
                    buf_action += '%s' % var
                else:
                    buf_action += '%s,' % var
            buf_action += ';\n'
        if len(self.string_var) != 0:
            buf_action += 'String '
            for var in self.string_var:
                if self.string_var.index(var) == len(self.string_var) - 1:
                    buf_action += '%s' % var
                else:
                    buf_action += '%s,' % var
            buf_action += ';\n'
        if len(self.boolean_var) != 0:
            buf_action += 'boolean '
            for var in self.boolean_var:
                if self.boolean_var.index(var) == len(self.boolean_var) - 1:
                    buf_action += '%s' % var
                else:
                    buf_action += '%s,' % var
            buf_action += ';\n'
        for paction in action:
            buf_action += '%s\n' % paction
        temp = []
        new = ''
        temp = buf_action.splitlines(True)
        i = 0
        while i < len(temp):
            temp[i] = '\t' + temp[i]
            new += temp[i]
            i = i + 1
        buf_action = new
        buf = 'function %s %s(%s) {\n' % (self.deffunction[function_name], function_name, parameter)
        buf = buf + buf_action
        buf += '}\n\n'
        if function_name == 'Leaf' or function_name == 'DataShortJudge':
            self.setDRL(ctx, '')
        else:
            self.setDRL(ctx, buf)
        self.construct = ''
        self.double_var = []
        self.string_var = []
        self.boolean_var = []
        self.var_name_list = []
        self.variable = {}
        self.deffunc_name = ''

    def exitSwitch_stmt(self, ctx: clipsparser.Switch_stmtContext):
        test_expr = self.getDRL(ctx.test_expression())
        buf = ''
        buf += 'switch (%s)\n{\n' % test_expr
        for case in ctx.case_stmt():
            buf += '%s' % self.getDRL(case)
        if ctx.default_stmt() != None:
            buf += '%s' % self.getDRL(ctx.default_stmt())
        else:
            if self.deffunc_name == 'NotifyOrNot':
                buf += 'default:\n\treturn false;\n'
        buf += '}\n'
        self.setDRL(ctx, buf)

    def exitTest_expression(self, ctx: clipsparser.Test_expressionContext):
        test_expr = ''
        if ctx.getChild(0).getRuleIndex() == 1:
            test_expr = '%s' % self.getDRL(ctx.variable())
        else:
            print("switch格式错误")
        self.setDRL(ctx, test_expr)

    def exitCase_stmt(self, ctx: clipsparser.Case_stmtContext):
        constant_expr = self.getDRL(ctx.comparison_expression())
        action = ''
        for paction in ctx.action():
            action += '%s\n' % self.getDRL(paction)
        # 按格式缩进case后action部分
        temp = []
        new = ''
        temp = action.splitlines(True)
        z = 0
        while z < len(temp):
            temp[z] = '\t' + temp[z]
            new += temp[z]
            z = z + 1
        action = new
        buf = 'case "%s":\n' % constant_expr
        buf += '%s' % action
        self.setDRL(ctx, buf)

    def exitDefault_stmt(self, ctx: clipsparser.Default_stmtContext):
        action = ''
        for paction in ctx.action():
            action += '%s\n' % self.getDRL(paction)
        buf = 'default:\n'
        buf += '%s' % action
        self.setDRL(ctx, buf)

    def exitComparison_expression(self, ctx: clipsparser.Comparison_expressionContext):
        constant_expr = '%s' % ctx.getText()
        self.setDRL(ctx, constant_expr)

    def enterDefrule(self, ctx: clipsparser.DefruleContext):
        self.construct = 'defrule'

    def exitAction(self, ctx: clipsparser.ActionContext):
        self.setDRL(ctx, self.getDRL(ctx.getChild(0)))

    def bind_constant(self, ctx, name, value, index):
        # 将基本数据类型付给新建变量
        # ctx:上下文对象 name：新建变量名 value：变量值 index：变量值在语法文件中标号
        if index == 118:  # int
            self.double_var.append(name)
            self.var_name_list.append(name)
        elif index == 119:  # float
            self.double_var.append(name)
            self.var_name_list.append(name)
        elif index == 120:  # symbol
            self.string_var.append(name)
            self.var_name_list.append(name)
            if value != 'null':
                value = '"%s"' % value
        elif index == 121:  # string
            self.string_var.append(name)
            self.var_name_list.append(name)
        return value

    def bind_variable(self, name1, name2):
        # 将已有变量值付给新建变量
        # name1:新建变量名 name2：赋值变量名
        if name2 in self.double_var:
            self.double_var.append(name1)
            self.var_name_list.append(name1)
        elif name2 in self.double_var:
            self.double_var.append(name1)
            self.var_name_list.append(name1)
        elif name2 in self.string_var:
            self.string_var.append(name1)
            self.var_name_list.append(name1)
        elif name2 in self.boolean_var:
            self.boolean_var.append(name1)
            self.var_name_list.append(name1)

    def bind_function_call(self, name, function_name, index):
        # 将函数返回值赋给新建变量
        buf = ''
        if index == 17:  # math_function
            self.double_var.append(name)
            self.var_name_list.append(name)
        elif index == 18:  # predicate_function
            self.boolean_var.append(name)
            self.var_name_list.append(name)
        elif index == 19:  # connected_function
            self.boolean_var.append(name)
            self.var_name_list.append(name)
        elif index == 16:  # tradition_function
            if function_name in self.deffunction:
                type = self.deffunction[function_name]
                if type == 'String':
                    self.string_var.append(name)
                    self.var_name_list.append(name)
                elif type == 'double':
                    self.double_var.append(name)
                    self.var_name_list.append(name)
                elif type == 'boolean':
                    self.boolean_var.append(name)
                    self.var_name_list.append(name)
                else:
                    pass

    def exitTradition_function(self, ctx: clipsparser.Tradition_functionContext):
        functionname = self.getDRL(ctx.function_name())
        buf = ''
        # bind函数
        if functionname == 'bind':
            if len(ctx.expression()) == 2:
                var_name = self.getDRL(ctx.expression(0))  # 赋值变量名
                var_value = self.getDRL(ctx.expression(1))  # 赋值内容
                if not (var_name in self.var_name_list):
                    if ctx.expression(1).getChild(0).getRuleIndex() == 123:  # 赋constant类型变量
                        index = ctx.expression(1).getChild(0).getChild(0).getRuleIndex()
                        ctx1 = ctx.expression(1).getChild(0).getChild(0)
                        var_value = self.bind_constant(ctx1, var_name, var_value, index)
                    elif ctx.expression(1).getChild(0).getRuleIndex() == 1:  # 赋已有变量
                        self.bind_variable(var_name, var_value)
                    elif ctx.expression(1).getChild(0).getRuleIndex() == 15:  # 赋表达式
                        index = ctx.expression(1).getChild(0).getChild(0).getRuleIndex()
                        function_name = ctx.expression(1).getChild(0).getChild(0).getChild(1).getText()
                        self.bind_function_call(var_name, function_name, index)
                    if var_value[0] == '(' and var_value[-1] == ')':
                        var_value = var_value[1:-1]
                    buf = '%s = %s;' % (var_name, var_value)
                else:
                    if ctx.expression(1).getChild(0).getRuleIndex() == 123:
                        if ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 121:
                            var_value = '"%s"' % var_value
                        elif ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 120 and var_value != 'null':
                            var_value = '"%s"' % var_value
                    if var_value[0] == '(' and var_value[-1] == ')':
                        var_value = var_value[1:-1]
                    buf = '%s = %s;' % (var_name, var_value)
            else:
                pass
        # assert函数
        elif functionname == 'assert':
            name = self.getDRL(ctx.expression(0).getChild(0).getChild(0).getChild(1))
            value = self.getDRL(ctx.expression(0).getChild(0).getChild(0).getChild(2))
            buf = 'modify( $p ) { %s = %s };' % (name, value)
            # 判断变量数据类型，并将其存入variable
            if not (name in self.variable):
                if ('$' + name) in self.string_var:
                    self.variable[name] = 'String'
                elif ('$' + name) in self.double_var:
                    self.variable[name] = 'double'
                elif ('$' + name) in self.boolean_var:
                    self.variable[name] = 'boolean'
                else:
                    try:
                        ctx.expression(1).getChild(0).getChild(0).getChild(0).getRuleIndex()
                    except AttributeError:
                        pass
                    else:
                        if (ctx.expression(0).getChild(0).getChild(0).getChild(0).getRuleIndex() == 120
                                or ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 121):
                            self.variable[name] = 'String'
                        elif (ctx.expression(0).getChild(0).getChild(0).getChild(0).getRuleIndex() == 118
                              or ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 119):
                            self.variable[name] = 'double'
        # load函数
        elif functionname == 'load':
            name = ctx.expression(0).getChild(0).getChild(0).getChild(3).getText()
            name = name[:-4] + 'drl"'
            self.load = 1
            if (self.filename != 'Entrance' and self.filename != 'MS_DietDataJudge'
                    and self.filename != 'MS_SportDataJudge'
                    and self.filename != 'MS_MSRiskDegreeEvaluation'):
                # buf = '$r.CurrentName.add( %s );\n' % name
                # buf += '$r.CurrentName.remove( "%s.drl");\n' % self.filename
                # buf += 'update($r);'
                buf += 'drools.setFocus("%s");' % name[1:-5]
                self.drool = 1

            else:
                # buf = '$r.CurrentName.add( %s );\n' % name
                # buf += 'update($r);'
                buf += 'drools.setFocus("%s");' % name[1:-5]
                self.drool = 1
            # buf += '$r.LastName.add( "%s.drl" );' % self.last_filename
        # strcat函数
        elif functionname == 'str-cat':
            buf = ''
            for expr in ctx.expression():
                if ctx.expression().index(expr) == len(ctx.expression()) - 1:
                    # 忽略filepath
                    if expr.getText() == '?FilePath':
                        buf += ''
                    else:
                        buf += '%s' % self.getDRL(expr)
                else:
                    # 忽略filepath
                    if expr.getText() == '?FilePath':
                        buf += ''
                    else:
                        buf += '%s + ' % self.getDRL(expr)
            buf = '(%s)' % buf
        # undefrule函数
        elif functionname == 'undefrule':
            buf = ''
        # Operatefact、Operatenumberfact函数
        elif functionname == 'OperateFact' or functionname == 'OperateNumberFact':
            name = self.getDRL(ctx.expression(0))
            value = self.getDRL(ctx.expression(1))
            try:
                ctx.expression(1).getChild(0).getChild(0).getRuleIndex()
            except AttributeError:
                pass
            else:
                if ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 120:
                    if value != 'null':
                        value = '"%s"' % value
            if name[0] == '"':
                name = name[1:-1]
            if self.construct == 'deffunction':
                buf = '$p.set%s(%s);' % (name, value)
            else:
                # 原始版本
                # buf = 'modify ($p) { %s = %s };' % (name, value)
                # 2019.12.19更新
                buf = ''
            # 判断变量数据类型，并将其存入variable
            if not (name in self.variable):
                # if ('$' + name) in self.string_var:
                #     self.variable[name] = 'String'
                # elif ('$' + name) in self.double_var:
                #     self.variable[name] = 'double'
                # elif ('$' + name) in self.boolean_var:
                #     self.variable[name] = 'boolean'
                if value in self.string_var:
                    self.variable[name] = 'String'
                elif value in self.double_var:
                    self.variable[name] = 'double'
                elif value in self.boolean_var:
                    self.variable[name] = 'boolean'
                else:
                    try:
                        ctx.expression(1).getChild(0).getChild(0).getRuleIndex()
                    except AttributeError:
                        pass
                    else:
                        if (ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 120
                                or ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 121):
                            self.variable[name] = 'String'
                        elif (ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 118
                              or ctx.expression(1).getChild(0).getChild(0).getRuleIndex() == 119):
                            self.variable[name] = 'double'

        elif functionname in self.deffunction:
            para = ''
            for expr in ctx.expression():
                if expr.getChild(0).getRuleIndex() == 123:
                    if expr.getChild(0).getChild(0).getRuleIndex() == 120:
                        if expr.getChild(0).getChild(0).boolen_symbol() == None:
                            if self.getDRL(expr) != 'null':
                                temp = '"%s"' % self.getDRL(expr)
                                self.setDRL(expr, temp)
            for expr in ctx.expression():
                if ctx.expression().index(expr) != len(ctx.expression()) - 1:
                    if expr.getText() == '?FilePath' or expr.getText() == '?filepath':
                        para += ''
                    else:
                        para += '%s,' % self.getDRL(expr)
                else:
                    if expr.getText() == '?FilePath' or expr.getText() == '?filepath':
                        para += ''
                    else:
                        if self.getDRL(expr)[1:-1] in self.beizhong_variable:
                            para += '"%s"' % self.beizhong_variable[self.getDRL(expr)[1:-1]]
                        else:
                            para += '%s' % self.getDRL(expr)
            if (functionname == 'DataNotify' or functionname == 'FileLoadNotify'):
                buf = '$r.%s( %s )' % (functionname, para)
            elif functionname == 'FactUsed':
                if self.load == 0:
                    # 原始版本
                    # buf = '$r.%s( %s );\n' % (functionname, para)
                    # buf += '$r.CurrentName.remove( "%s.drl");\n' % self.filename
                    # 2019.12.19更新'
                    # buf = '$r.CurrentName.remove( "%s.drl");\n' % self.filename
                    # buf += 'update($r)'
                    buf = ''
                else:
                    # 原始版本
                    # buf = '$r.%s( %s )' % (functionname, para)
                    buf = ''
            elif functionname == 'InterpretationIndex':
                # buf = '$r.%s( %s,"%s.drl" )' % (functionname, para, self.filename)
                # 2019.12.19修改
                buf = ''
            elif functionname == 'Recommendation':
                self.Recommendation = 1
                self.description = 1
                self.formatText_number += 1
                buf = 'FormatText $formatText%s = new FormatText();\n' % self.formatText_number
                buf += '$formatText%s.setValue( %s )' % (self.formatText_number, para)
            elif (functionname == 'Check' or functionname == 'NotifyOrNot'):
                buf = '$f.%s( $r,%s )' % (functionname, para)
                if functionname == 'NotifyOrNot':
                    self.NotifyOrNot = 1
            elif functionname == 'Leaf':
                buf = '$f.%s( %s )' % (functionname, para)
            elif functionname == 'Transform':
                buf = '$f.%s( %s )' % (functionname, para)
            elif functionname == 'AddOrNot':
                buf = '$f.%s( %s )' % (functionname, para)
            elif functionname == 'DataShortJudge':
                buf = '$f.%s( $r,%s )' % (functionname, para)
            elif functionname == 'ConfirmGlucoseLevel':
                buf = '%s( $p,%s )' % (functionname, para)
            else:
                buf = '%s( %s )' % (functionname, para)
            try:
                ctx.parentCtx.parentCtx.parentCtx.getRuleIndex()
            except AttributeError:
                pass
            else:
                if ctx.parentCtx.parentCtx.parentCtx.getRuleIndex() == 3:
                    if buf != '':
                        buf = '%s;' % buf
        else:
            attr_value = self.getDRL(ctx.getChild(2))
            attr_name = functionname
            if attr_name == None or attr_name[0] != '"':
                attr_name = attr_name
            else:
                attr_name = attr_name[1:-1]
            buf = '%s = %s' % (attr_name, attr_value)
        self.setDRL(ctx, buf)

    def exitReturn_stmt(self, ctx: clipsparser.Return_stmtContext):
        parameter = ''
        if ctx.expression().getText() != None:
            parameter = self.getDRL(ctx.expression())
        buf = 'return %s;' % parameter
        self.setDRL(ctx, buf)

    def enterDeffunction(self, ctx: clipsparser.DeffunctionContext):
        self.construct = 'deffunction'
        if ctx.symbol_expression().getText() == 'NotifyOrNot':
            self.deffunc_name = 'NotifyOrNot'

    def exitOrdered_pattern(self, ctx: clipsparser.Ordered_patternContext):
        x = ''
        attr_name = self.getDRL(ctx.symbol_expression())
        attr_value = self.getDRL(ctx.constaint(0))
        self.var_name_list.append(attr_value)
        if not (attr_name in self.variable):
            self.variable[attr_name] = 'String'
        # 变量强制类型转换
        # set方法后属性名第一个字母大写，现在暂时没管
        captital_name = attr_name[0].capitalize() + attr_name[1:]
        lower_name = attr_name[0].lower() + attr_name[1:]
        if attr_name in self.data_model:
            if self.data_model[attr_name] == 'PatientInfo' or self.data_model[attr_name] == 'VisitInfo':
                if self.patient_variable[attr_name] == 'double':
                    self.convert_string += 'double %s = 0;\n' % attr_value
                    self.convert_string += 'if ($%s.get%s() != null) {\n' % (
                        self.data_model[attr_name], captital_name)
                    self.convert_string += '\t%s = Double.parseDouble( $%s.get%s() );\n' % (
                        attr_value, self.data_model[attr_name], captital_name)
                    self.convert_string += '}\n'

            elif self.data_model[attr_name] == 'LabTestResult':
                if self.patient_variable[attr_name] == 'double':
                    self.convert_string += 'double %s = 0;\n' % attr_value
                    if attr_name in self.beizhong_variable:
                        self.convert_string += 'if (!($Patient.getLabTestResult("%s").getResult().equals(""))) {\n' % (
                            self.beizhong_variable[attr_name])
                        self.convert_string += '\t%s = Double.parseDouble( $Patient.getLabTestResult("%s").getResult(' \
                                               ') );\n' % (attr_value, self.beizhong_variable[attr_name])
                    else:
                        self.convert_string += 'if (!($Patient.getLabTestResult("%s").getResult().equals(""))) {\n' % (
                            attr_name)
                        self.convert_string += '\t%s = Double.parseDouble( $Patient.getLabTestResult("%s").getResult(' \
                                               ') );\n' % (attr_value, attr_name)
                    self.convert_string += '}\n'
                elif self.patient_variable[attr_name] == 'String':
                    self.convert_string += 'String %s = $LabTestResult_%s.getResult();\n' % (
                        attr_value, attr_name)
            elif self.data_model[attr_name] == 'PastHistory':
                if self.patient_variable[attr_name] == 'String':
                    if attr_name in self.beizhong_variable:
                        self.convert_string += 'String %s = (!$pasthistory_diagnosis_%s.isEmpty())? "YES":"NO";\n' % (
                            attr_value, self.beizhong_variable[attr_name])
                    else:
                        self.convert_string += 'String %s = (!$pasthistory_diagnosis_%s.isEmpty())? "YES":"NO";\n' % (
                            attr_value, attr_name)
            elif self.data_model[attr_name] == 'FamilyHistory':
                if self.patient_variable[attr_name] == 'String':
                    if attr_name in self.beizhong_variable:
                        self.convert_string += 'String %s = (!$familyhistory_diagnosis_%s.isEmpty())? "YES":"NO";\n' % (
                            attr_value, self.beizhong_variable[attr_name])
                    else:
                        self.convert_string += 'String %s = (!$familyhistory_diagnosis_%s.isEmpty())? "YES":"NO";\n' % (
                            attr_value, attr_name)
            elif self.data_model[attr_name] == 'PhysicalSign':
                if self.patient_variable[attr_name] == 'double':
                    self.convert_string += 'double %s = 0;\n' % attr_value
                    if attr_name in self.beizhong_variable:
                        self.convert_string += 'if (!($Patient.getPhysicalSign("%s").getValue().equals(""))) {\n' % (
                            self.beizhong_variable[attr_name])
                        self.convert_string += '\t%s = Double.parseDouble( $Patient.getPhysicalSign("%s").getValue() ' \
                                               ');\n' % (attr_value, self.beizhong_variable[attr_name])
                    else:
                        self.convert_string += 'if (!($Patient.getPhysicalSign("%s").getValue().equals(""))) {\n' % (
                            attr_name)
                        self.convert_string += '\t%s = Double.parseDouble( $Patient.getPhysicalSign("%s").getValue() ' \
                                               ');\n' % (attr_value, attr_name)
                    self.convert_string += '}\n'
                else:
                    if attr_name in self.beizhong_variable[attr_name]:
                        self.convert_string += 'Sring %s = $Patient.getPhysicalSign("%s").getValue();\n' \
                                               % (attr_value, self.beizhong_variable[attr_name])
                    else:
                        self.convert_string += 'Sring %s = $Patient.getPhysicalSign("%s").getValue();\n' \
                                               % (attr_value, attr_name)

            elif self.data_model[attr_name] == 'Order':
                if self.patient_variable[attr_name] == 'String':
                    self.convert_string += 'String %s = "NO";\n' % attr_value
                    # 数据模型替换
                    if attr_name in self.beizhong_variable:
                        self.convert_string += 'if ($Patient.getOrder("%s").getPerformResult().equals("YES")) {\n' % (
                            self.beizhong_variable[attr_name])
                    else:
                        self.convert_string += 'if ($Patient.getOrder("%s").getPerformResult().equals("YES")) {\n' % (
                            attr_name)
                    self.convert_string += '\t%s = "YES";\n' % attr_value
                    self.convert_string += '}\n'
            elif self.data_model[attr_name] == 'Diagnosis':
                # if self.patient_variable[attr_name] == 'String':
                #     self.convert_string += 'String %s = "";\n' % attr_value
                #     self.convert_string += 'for (i=0;i<$Patient.getDiagnosisList().size();i++) {\n'
                #     self.convert_string += '\ttemp = $Patient.getDiagnosisList().get(0).getItemName().split("/");\n'
                #     self.convert_string += '\tfor(j=0;j<temp.length;j++){\n'
                #     self.convert_string += '\t\tif(temp[0].equals("%s")){\n' % attr_name
                #     self.convert_string += '\t\t\t%s = temp[1];\n' % attr_value
                #     self.convert_string += '\t\t'
                pass
        try:
            ctx.constaint(0).getChild(0).getChild(0).getChild(0).getChild(0).getChild(0).getRuleIndex()
        except AttributeError:
            if attr_name in self.patient_variable:
                # 更新后
                if attr_name in self.data_model:
                    if self.data_model[attr_name] == 'PatientInfo':
                        x = '$patientInfo : patientInfo != null'
                        x += '\n'
                        if self.patient_variable[attr_name] != 'String':
                            x += 'PatientInfo( %s != null ) from $patientInfo' % lower_name
                        else:
                            x += 'PatientInfo( %s : %s != null ) from $patientInfo' % (attr_value, lower_name)
                    elif self.data_model[attr_name] == 'VisitInfo':
                        x = 'visitInfo : visitInfo != null'
                        x += '\n'
                        if self.patient_variable[attr_name] != 'String':
                            x += 'VisitInfo( %s != null ) from $visitInfo' % lower_name
                        else:
                            x += 'VisitInfo( %s : %s != null ) from $visitInfo' % (attr_value, lower_name)
                    elif self.data_model[attr_name] == 'LabTestResult':
                        x = '$labTestResultList : labTestResultList != null'
                        x += '\n'
                        # 北肿数据
                        if attr_name in self.beizhong_variable:
                            x += '$LabTestResult_%s : LabTestResult( itemName == "%s" ) from $labTestResultList' % (
                                self.beizhong_variable[attr_name], self.beizhong_variable[attr_name])
                        else:
                            x += '$LabTestResult_%s : LabTestResult( itemName == "%s" ) from $labTestResultList' % (
                                attr_name, attr_name)
                    # 待调整
                    elif self.data_model[attr_name] == 'PastHistory':
                        self.history = 1
                        x = '$pastHistoryList : pastHistoryList != null'
                        x += '\n'
                        x += '$pasthistory_diagnosis : ArrayList( size > -1 )\n'
                        x += '\t\tfrom accumulate( PastHistory($items : items) from $pastHistoryList,\n'
                        x += '\t\t\t\tinit( ArrayList past_arrayList = new ArrayList(); ),\n'
                        x += '\t\t\t\taction( past_arrayList.addAll($items);),\n'
                        x += '\t\t\t\tresult( past_arrayList) )\n'
                        # 数据模型替换
                        if attr_name in self.beizhong_variable:
                            x += '$pasthistory_diagnosis_%s : ArrayList() from collect (Diagnosis(itemName == "%s") ' \
                                 'from $pasthistory_diagnosis)' % (self.beizhong_variable[attr_name],
                                                                   self.beizhong_variable[attr_name])
                        else:
                            x += '$pasthistory_diagnosis_%s : ArrayList() from collect (Diagnosis(itemName == "%s") ' \
                                 'from $pasthistory_diagnosis)' % (attr_name, attr_name)

                    elif self.data_model[attr_name] == 'FamilyHistory':
                        self.history = 1
                        x = '$familyHistoryList : familyHistoryList != null'
                        x += '\n'
                        x += '$familyhistory_diagnosis : ArrayList( size > -1 )\n'
                        x += '\t\tfrom accumulate( FamilyHistory($diagnoses : diagnoses) from $familyHistoryList,\n'
                        x += '\t\t\t\tinit( ArrayList family_arrayList = new ArrayList(); ),\n'
                        x += '\t\t\t\taction( family_arrayList.addAll($diagnoses);),\n'
                        x += '\t\t\t\tresult( family_arrayList) )\n'
                        # 数据模型替换
                        if attr_name in self.beizhong_variable:
                            x += '$familyhistory_diagnosis_%s : ArrayList() from collect (Diagnosis(itemName == "%s") ' \
                                 'from $familyhistory_diagnosis)' % (
                                     self.beizhong_variable[attr_name], self.beizhong_variable[attr_name])
                        else:
                            x += '$familyhistory_diagnosis_%s : ArrayList() from collect (Diagnosis(itemName == "%s") ' \
                                 'from $familyhistory_diagnosis)' % (attr_name, attr_name)

                    elif self.data_model[attr_name] == 'PhysicalSign':
                        x = '$physicalSignList : physicalSignList != null'
                        x += '\n'
                        # 数据模型替换
                        if attr_name in self.beizhong_variable:
                            x += '$PhysicalSign_%s : PhysicalSign( itemName == "%s") from $physicalSignList' % (
                                self.beizhong_variable[attr_name], self.beizhong_variable[attr_name])
                        else:
                            x += '$PhysicalSign_%s : PhysicalSign( itemName == "%s") from $physicalSignList' % (
                                attr_name, attr_name)

                    elif self.data_model[attr_name] == 'Order':
                        x = '$orderList : orderList != null'
                        x += '\n'
                        # 数据模型替换
                        if attr_name in self.beizhong_variable:
                            x += '$order_%s : Order(text=="%s") from $orderList' \
                                 % (self.beizhong_variable[attr_name], self.beizhong_variable[attr_name])
                        else:
                            x += '$order_%s : Order(text=="%s") from $orderList' % (attr_name, attr_name)

                    elif self.data_model[attr_name] == 'Diagnosis':
                        x = '$diagnosisList : diagnosisList != null'
                        x += '\n'
                        x += 'Diagnosis( %s : itemName != null ) from $diagnosisList' % attr_value
                # 待修改--------------------------------------------------------------------
                # --------------------------------------------------------------------------
                else:
                    self.mis_var[attr_name] = attr_value
                    x = ''
            else:
                x = '%s : %s != null' % (attr_value, attr_name)
        else:
            if (ctx.constaint(0).getChild(0).getChild(0).getChild(0).getChild(0).
                    getChild(0).getRuleIndex()) == 120:
                if attr_value == 'null':
                    if attr_name in self.patient_variable:
                        if self.patient_variable[attr_name] == 'double':
                            x = '%s == 0' % (attr_name)
                        else:
                            x = '%s == %s' % (attr_name, attr_value)
                    else:
                        x = '%s == %s' % (attr_name, attr_value)
                else:
                    x = '%s == "%s"' % (attr_name, attr_value)
            else:
                x = '%s == %s' % (attr_name, attr_value)
        self.setDRL(ctx, x)

    def exitMath_function(self, ctx: clipsparser.Math_functionContext):
        list_clisp_math = ['+', '-', '/', 'div', 'mod', '*']
        list_drools_math = ['+', '-', '/', '/', '%', '*']
        mathname = self.getDRL(ctx.math_name())
        # math函数
        i = 0
        op = []
        j = list_clisp_math.index(mathname)
        # 将所有操作数放入列表中
        for child in ctx.getChildren():
            if i > 1 and i < (len(ctx.children) - 1):
                op.append(self.getDRL(child))
            i = i + 1
        if mathname == '/':
            expr = '((double)%s ' % op[0]
            for xop in op[1:]:
                expr += ('%s (double)%s' % (list_drools_math[j], xop))
            expr += ')'
            self.setDRL(ctx, expr)
        elif mathname == 'div':
            expr = '((int)%s ' % op[0]
            for xop in op[1:]:
                expr += ('%s (int)%s' % (list_drools_math[j], xop))
            expr += ')'
            self.setDRL(ctx, expr)
        else:
            expr = '(%s ' % op[0]
            for xop in op[1:]:
                expr += ('%s %s' % (list_drools_math[j], xop))
            expr += ')'
            self.setDRL(ctx, expr)

    def exitPredicate_function(self, ctx: clipsparser.Predicate_functionContext):
        predicatename = self.getDRL(ctx.predicate_name())
        list_clips_predict = ['eq', 'neq', 'mod', '>', '<', '>=', '<=', '=']
        list_drools_predict = ['==', '!=', '%', '>', '<', '>=', '<=', '==']
        # predicate_name
        i = 0
        op = []
        j = list_clips_predict.index(predicatename)
        # 将所有操作数放入列表中
        for child in ctx.expression():
            if child.getChild(0).getRuleIndex() == 123:
                if child.getChild(0).getChild(0).getRuleIndex() == 120:
                    if self.getDRL(child) != 'null':
                        temp = '"%s"' % self.getDRL(child)
                        self.setDRL(child, temp)
            op.append(self.getDRL(child))
        expr = ''
        for xop in op[1:]:
            if len(op) > 2:
                if op[0] in self.double_var:
                    if xop == 'null':
                        xop = 0
                elif op[0][1:] in self.patient_variable:
                    if self.patient_variable[op[0][1:]] == 'double':
                        if xop == 'null':
                            xop = 0
                expr += ('%s %s %s' % (op[0], list_drools_predict[j], xop))
                if op.index(xop) != (len(op) - 1):
                    expr += ' && '
            else:
                if op[0] in self.double_var:
                    if xop == 'null':
                        xop = 0
                elif op[0][1:] in self.patient_variable:
                    if self.patient_variable[op[0][1:]] == 'double':
                        if xop == 'null':
                            xop = 0
                expr += ('%s %s %s' % (op[0], list_drools_predict[j], xop))
        expr = '%s' % expr
        self.setDRL(ctx, expr)

    def exitConnected_function(self, ctx: clipsparser.Connected_functionContext):
        list_clips_connect = ['and', 'or', 'not']
        list_drools_connect = ['&&', '||', '!']
        connectname = self.getDRL(ctx.connected_name())
        if connectname == 'not':
            name = list_drools_connect[list_clips_connect.index(connectname)]
            expr = self.getDRL(ctx.getChild(2))
            buf = '%s(%s)' % (name, expr)
            self.setDRL(ctx, buf)
        else:
            name = list_drools_connect[list_clips_connect.index(connectname)]
            op = []
            for child in ctx.expression():
                op.append(self.getDRL(child))
            if len(op) == 1:
                expr = '%s' % op[0]
            else:
                expr = '%s' % op[0]
                for xop in op[1:]:
                    expr += ' %s %s' % (name, xop)
            buf = '%s' % expr
            self.setDRL(ctx, buf)

    def exitConstant_expression(self, ctx: clipsparser.Constant_expressionContext):
        self.setDRL(ctx, self.getDRL(ctx.getChild(0)))

    def exitPattern_ce(self, ctx: clipsparser.Pattern_ceContext):
        self.setDRL(ctx, self.getDRL(ctx.ordered_pattern()))

    def exitConstaint(self, ctx: clipsparser.ConstaintContext):
        self.setDRL(ctx, self.getDRL(ctx.connected_constraint()))

    def exitConnected_constraint(self, ctx: clipsparser.Connected_constraintContext):
        self.setDRL(ctx, self.getDRL(ctx.single_constraint()))

    def exitSingle_constraint(self, ctx: clipsparser.Single_constraintContext):
        self.setDRL(ctx, self.getDRL(ctx.term()))

    def exitConditional_element(self, ctx: clipsparser.Conditional_elementContext):
        self.setDRL(ctx, self.getDRL(ctx.pattern_ce()))

    def exitProcedural_function(self, ctx: clipsparser.Procedural_functionContext):
        self.setDRL(ctx, self.getDRL(ctx.getChild(0)))

    def exitFunction_call(self, ctx: clipsparser.Function_callContext):
        self.setDRL(ctx, self.getDRL(ctx.getChild(0)))

    def exitFunction_name(self, ctx: clipsparser.Function_nameContext):
        self.setDRL(ctx, self.getDRL(ctx.getChild(0)))

    def exitMath_name(self, ctx: clipsparser.Math_nameContext):
        self.setDRL(ctx, ctx.getText())

    def exitConnected_name(self, ctx: clipsparser.Connected_nameContext):
        self.setDRL(ctx, ctx.getText())

    # 注释翻译
    def exitExpression_COMMENT(self, ctx: clipsparser.Expression_COMMENTContext):
        buf = ctx.getText()
        buf = buf.replace(buf[0], '//')
        buf.encode('UTF-8')

        buf = buf[:-2] + '\n'
        if ctx.parentCtx.getRuleIndex() == 21 or ctx.parentCtx.getRuleIndex() == 3:
            buf = buf[:-2]
        self.setDRL(ctx, buf)

    def exitExpression_functioncall(self, ctx: clipsparser.Expression_functioncallContext):
        self.setDRL(ctx, self.getDRL(ctx.function_call()))

    def exitExpression_constant(self, ctx: clipsparser.Expression_constantContext):
        self.setDRL(ctx, self.getDRL(ctx.constant_expression()))

    def exitExpression_variable(self, ctx: clipsparser.Expression_variableContext):
        self.setDRL(ctx, self.getDRL(ctx.variable()))

    def exitExpression_predicate_name(self, ctx: clipsparser.Expression_predicate_nameContext):
        self.setDRL(ctx, self.getDRL(ctx.predicate_name()))

    def exitPredicate_name(self, ctx: clipsparser.Predicate_nameContext):
        buf = ctx.getText()
        # 判断是否为traditon_funciton子节点
        try:
            ctx.parentCtx.parentCtx.getRuleIndex()
        except AttributeError:
            pass
        else:
            if ctx.parentCtx.parentCtx.getRuleIndex() == 16:
                buf = '"%s"' % buf
        self.setDRL(ctx, buf)

    def exitVariable(self, ctx: clipsparser.VariableContext):
        buf = ctx.getText()
        if buf[0] == '?':
            buf = buf.replace('?', '$', 1)
        self.setDRL(ctx, buf)

    def exitParameter(self, ctx: clipsparser.ParameterContext):
        # 自定义函数名
        function_name = self.getDRL(ctx.parentCtx.symbol_expression())
        buf = ''
        if function_name == 'Check':
            # buf = 'Result $r,String $ShortData,String $FilePath,String $FileName'
            # 修改后2019.12.21
            buf = 'Result $r,String $ShortData,String $FileName'
        elif function_name == 'Transform':
            buf = 'String $CValue'
        elif function_name == 'NotifyOrNot':
            # buf = 'Result $r,String $Relation,double $T,double $TValue,String $ShortData,String $FilePath,String $FileName'
            # 修改后2019.12.21
            buf = 'Result $r,String $Relation,double $T,double $TValue,String $ShortData,String $FileName'
        elif function_name == 'AddOrNot':
            buf = 'String $ShortData,String $Output'
        # elif function_name == 'DataShortJudge':
        #     buf = 'Result $r,String $InputData,String $DataName'
        elif function_name == 'FamilyHis':
            buf = 'String $FamilyHisItem,String $FamilyHisValue,double $FamilyHisNum'
        elif function_name == 'His':
            buf = 'String $HisItem,String $HisValue,double $HisNum'
        elif function_name == 'DataNotify':
            pass
        # elif function_name == 'Leaf':
        #   buf = 'String ?Relation,double ?T,double ?TValue,String ?ShortData,String ?FilePath,String ?FileName'
        elif function_name == 'FourInFiveOut':
            buf = 'double $InputNum'
        elif function_name == 'ConfirmGlucoseLevel':
            buf = 'Patient $p,double $Coeff,double $Lower,double $Upper'
        elif function_name == 'InterpretationIndex':
            pass
        elif function_name == 'Recommendation':
            pass
        elif function_name == 'FactUsed':
            pass
        self.setDRL(ctx, buf)

    def exitRegular_para(self, ctx: clipsparser.Regular_paraContext):
        self.setDRL(ctx, ctx.getText())

    def exitWildcard_para(self, ctx: clipsparser.Wildcard_paraContext):
        self.setDRL(ctx, ctx.getText())

    def exitSymbol_expression(self, ctx: clipsparser.Symbol_expressionContext):
        if self.construct == 'deffunction':
            try:
                ctx.parentCtx.getRuleIndex()
            except AttributeError:
                pass
            else:
                if ctx.parentCtx.getRuleIndex() == 85:
                    self.deffunction_name = ctx.getText()
        buf = ctx.getText()
        if ctx.boolen_symbol() != None:
            self.setDRL(ctx, self.getDRL(ctx.boolen_symbol()))
        else:
            self.setDRL(ctx, buf)

    def exitString_expression(self, ctx: clipsparser.String_expressionContext):
        buf = ctx.getText()
        # 判断字符串中是否含换行符
        list = buf.splitlines()
        temp = ''
        if len(list) > 1:
            for plist in list:
                if list.index(plist) == len(list) - 1:
                    temp += '+ "%s' % plist
                elif list.index(plist) == 0:
                    temp += '%s"\n' % plist
                else:
                    temp += '+ "%s"\n' % plist
            buf = temp
        self.setDRL(ctx, buf)

    def exitInteger_expression(self, ctx: clipsparser.Integer_expressionContext):
        self.setDRL(ctx, ctx.getText())

    def exitFloat_expression(self, ctx: clipsparser.Float_expressionContext):
        self.setDRL(ctx, ctx.getText())

    def exitBoolen_symbol(self, ctx: clipsparser.Boolen_symbolContext):
        buf = '%s' % ctx.getText()
        buf = '%s' % buf.lower()
        self.setDRL(ctx, buf)

    def exitRule_name(self, ctx: clipsparser.Rule_nameContext):
        self.setDRL(ctx, ctx.getText())

    def exitTerm(self, ctx: clipsparser.TermContext):
        buf = ctx.getText()
        if buf[0] == '?':
            buf = buf.replace('?', '$', 1)
        self.setDRL(ctx, buf)

    def exitProg(self, ctx: clipsparser.ProgContext):
        buf = ''
        for child in ctx.getChildren():
            buf += '%s' % self.getDRL(child)
        self.setDRL(ctx, buf)

    def exitConstruct(self, ctx: clipsparser.ConstructContext):
        buf = ''
        for child in ctx.getChildren():
            buf += '%s' % self.getDRL(child)
        self.setDRL(ctx, buf)
