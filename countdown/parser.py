"""File that contains the Parser class."""
from lark import Lark, Transformer
from countdown.expression import Add, Multiply, Subtract, Divide, Number,  Expression


# --------------------
# Grammar definition for our Expressions, as needed for the
# Lark parser.
#
# Documentation: https://github.com/lark-parser/lark
# Example: https://github.com/lark-parser/lark/blob/master/docs/json_tutorial.md
# --------------------
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
    """
    Transformer to convert the tokens generated by the parser into our
    Expression classes.
    """
    def expr(self, values):
        """
        Convert the expr's from the grammar definition into Adds and
        Subtracts.

        :param values: supplied by parser
        :return: Expression
        """
        if len(values) == 3:
            term1, op, term2 = values
            if op == "+":
                return Add(term1, term2)
            else:
                return Subtract(term1, term2)

        (num,) = values
        return num

    def term(self, values):
        """
        Convert the term's from the grammar definition into Multiplies and
        Divides.

        :param values: supplied by parser
        :return: Expression
        """
        if len(values) == 3:
            factor1, op, factor2 = values
            if op == "*":
                return Multiply(factor1, factor2)
            else:
                return Divide(factor1, factor2)

        (num,) = values
        return num

    def base(self, values):
        """
        Convert the bases's from the grammar definition into Numbers.

        :param values: supplied by parser
        :return: Expression
        """
        if len(values) == 3:
            lparen, expr, rparen = values
            return expr

        (num,) = values
        return Number(int(num))


class Parser:
    """
    Class that allows us to parse strings into Expression objects.
    This functions as a wrapper around the messy Lark code.
    """
    def __init__(self):
        self._parser = _expression_parser
        self._transformer = _TreeToExpression()

    def parse(self, expression_str) -> Expression:
        """
        Parse the input string into an Expression.

        :param expression_str: input string
        :return: a valid Expression
        """
        tree = self._parser.parse(expression_str)
        return self._transformer.transform(tree)
