
from lark import Lark, Transformer
from countdown.expression import Add, Multiply, Subtract, Divide, Number


_expression_parser = Lark(r"""
    expr    : expr PLUS term
            | expr MINUS term
            | term
            
    term    : term TIMES base
            | term DIVIDES base
            | base
    
    base    : INT
            | LPAREN expr RPAREN
    
    PLUS    : "+"
    DIVIDES : "/"
    MINUS   : "-"
    TIMES   : "*"
    
    LPAREN  : "("
    RPAREN  : ")"
    
    %import common.INT
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

    def base(self, values):
        if len(values) == 3:
            lparen, expr, rparen = values
            return expr

        (num,) = values
        return Number(int(num))


class Parser:
    def __init__(self):
        self._parser = _expression_parser
        self._transformer = _TreeToExpression()

    def parse(self, expression_str):
        tree = self._parser.parse(expression_str)
        return self._transformer.transform(tree)
