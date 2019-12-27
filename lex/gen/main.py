from antlr4 import *
from io import StringIO
from typing import TextIO
from gen.clipslexer import clipslexer
from gen.clipsparser import clipsparser
from gen.clipsparserListener import clipsparserListener
from gen.clipsparserbaselistener import clipsparserbaselistener
from string import Template


def main():
    f = FileStream("new2.clp", 'ansi', 'strict')  # 输入文件
    lexer = clipslexer(f)
    tokens = CommonTokenStream(lexer)
    parser = clipsparser(tokens)
    a = parser.prog()  # 语法分析树
    listener = clipsparserbaselistener()
    walker = ParseTreeWalker()
    walker.walk(listener, a)  # 遍历语法分析树
    print(a.toStringTree([], parser))


if __name__ == '__main__':
    main()

    # if_then_else中嵌套额外if_then_else
    '''
        elif ctx.parentCtx.parentCtx.parentCtx.parentCtx.parentCtx.getRuleIndex() == 21 and self.construct == 'defrule':
            expression = self.getDRL(ctx.expression())
            action1 = ''
            action2 = ''
            if (ctx.ELSE() == None):
                for pctx in ctx.action():
                    action1 += self.getDRL(pctx)
            else:
                i = 0
                for child in ctx.getChildren():
                    if child == ctx.ELSE():
                        add = i
                    i += 1
                j = ctx.getChildCount() - 1
                i = 0
                for child in ctx.getChildren():
                    if i > 3 and i < add:
                        action1 += self.getDRL(child)
                    if i > add and i < j:
                        action2 += self.getDRL(child)
                    i = i + 1
            buf = 'rule ' + ('"%s%s-%s" ' % (self.rule,(self.num1 + 1), self.num2)) + 'extends' + (' "%s%s"\n' % (self.rule,(self.num1 + 1)))
            buf += 'sailence %s\n' % (self.sailence2)
            buf += 'when\n'
            buf += ('$p: Patient%s ' % expression) + '\n'
            buf += 'then\n'
            buf += ('%s\n' % action1)
            buf += 'end\n\n'
            self.son_son_rule += '%s' % buf
            # 判断是否存在else结构
            if (ctx.ELSE() != None):
                self.num2 += 1
                self.sailence2 -= 1
                buf_else = 'rule ' + ('"%s%s-%s" ' % (self.rule,(self.num1 + 1), self.num2)) + 'extends' + (' "%s%s"\n' % (self.rule,(self.num1 + 1)))
                buf_else += 'sailence %s\n' % (self.sailence2)
                buf_else += 'when\n'
                buf_else += ('not($p: Patient%s ' % expression) + ')\n'
                buf_else += 'then\n'
                buf_else += ('%s\n' % action2)
                buf_else += 'end\n\n'
                self.son_son_rule += '%s' % buf_else
            self.num2 = 0'''
