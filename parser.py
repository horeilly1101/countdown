
from lark import Lark, Transformer
from expression import Add, Multiply, Subtract, Divide


expression_parser = Lark(r"""
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


class TreeToExpression(Transformer):
    def expr(self, values):
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


if __name__ == "__main__":
    text = '89+90+9+   8* 78'
    tree = expression_parser.parse(text)
    print(TreeToExpression().transform(tree))
    # print( json_parser.parse(text).pretty() )
