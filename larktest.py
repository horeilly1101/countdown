
from lark import Lark, Transformer
from expression import Add, Subtract

json_parser = Lark(r"""
    add: (  )

    list : "[" [value ("," value)*] "]"

    dict : "{" [pair ("," pair)*] "}"
    pair : string ":" value

    string : ESCAPED_STRING

    %import common.ESCAPED_STRING
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS

    """, start='value')


class TreeToJson(Transformer):
    def string(self, s):
        (s,) = s
        return s[1:-1]
    def number(self, n):
        (n,) = n
        return float(n)

    list = list
    pair = tuple
    dict = dict

    null = lambda self, _: None
    true = lambda self, _: True
    false = lambda self, _: False


if __name__ == "__main__":
    text = '{"key": ["item0", "item1", 3.14, true]}'
    tree = json_parser.parse(text)
    print(TreeToJson().transform(tree)["key"])
    # print( json_parser.parse(text).pretty() )
