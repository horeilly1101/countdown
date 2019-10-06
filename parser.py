
from lark import Lark, Transformer
from expression import Add, Multiply, Subtract, Divide


_expression_parser = Lark(r"""
    expr    : expr PLUS term
            | expr MINUS term
            | term
            
    term    : term TIMES NUMBER
            | term DIVIDES NUMBER
            | NUMBER
    
    PLUS    : "+"
    DIVIDES : "/"
    MINUS   : "-"
    TIMES   : "*"
    
    %import common.NUMBER
    %import common.WS
    %ignore WS
    """, start='expr')


class _TreeToExpression(Transformer):
    def expr(self, values):
        # in this
        if len(values) == 3:
            term1, op, term2 = values
            if op == "+":
                return Add(term1, term2)
            else:
                return Subtract(term1, term2)

        (num,) = values
        return num

    def term(self, values):
        if len(values) == 3:
            factor1, op, factor2 = values
            if op == "*":
                return Multiply(factor1, factor2)
            else:
                return Divide(factor1, factor2)

        (num,) = values
        return num

    def number(self, num):
        (num,) = num
        return int(num)


class Parser:
    def __init__(self):
        self._parser = _expression_parser
        self._transformer = _TreeToExpression()

    def parse(self, expression_str):
        tree = self._parser.parse(expression_str)
        return self._transformer.transform(tree)
