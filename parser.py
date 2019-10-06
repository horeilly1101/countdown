# from typing import List, NamedTuple
#
#
# class _Token:
#     def __init__(self, character):
#         self.character = character
#
#     def __str__(self):
#         return str(self.character)
#
#
# PLUS = _Token("+")
# MINUS = _Token("-")
# TIMES = _Token("*")
# DIVIDE = _Token("/")
# OPEN_PAREN = _Token("(")
# CLOSE_PAREN = _Token(")")
#
#
# class Number(_Token):
#     def __init__(self, character):
#         super().__init__(character)
#
#
# class Scanner:
#     _INT_MAP = {
#         num_str: int(num_str)
#         for num_str in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#     }
#
#     def __init__(self, user_input: str):
#         self.user_input = user_input
#
#     def _scan_integer_from(self, idx) -> list:
#         number = 0
#         new_idx = idx
#
#         for char in self.user_input[idx:]:
#             if char in self._INT_MAP:
#                 number = number * 10 + self._INT_MAP[char]
#                 new_idx = new_idx + 1
#             else:
#                 break
#
#         return self._scan_from(new_idx) + [Number(number)]
#
#     def _scan_from(self, idx) -> list:
#         # base case, when all characters have been scanned
#         if idx >= len(self.user_input):
#             return []
#
#         character = self.user_input[idx]
#
#         if character in self._INT_MAP:
#             return self._scan_integer_from(idx)
#
#         if character == "+":
#             return self._scan_from(idx + 1) + [PLUS]
#
#         if character == "-":
#             return self._scan_from(idx + 1) + [MINUS]
#
#         if character == "*":
#             return self._scan_from(idx + 1) + [TIMES]
#
#         if character == "/":
#             return self._scan_from(idx + 1) + [DIVIDE]
#
#         if character == "(":
#             return self._scan_from(idx + 1) + [OPEN_PAREN]
#
#         if character == ")":
#             return self._scan_from(idx + 1) + [CLOSE_PAREN]
#
#         raise ValueError("Couldn't match the character!")
#
#     def scan(self):
#         return reversed(self._scan_from(0))
#
#     def validate(self, numbers: List[int]):
#
#
#
# class ParserState(NamedTuple):
#     next_idx: int
#     expression: "Expression"
#     success: bool
#
#     def get_next_character(self, user_input):
#         return user_input[self.next_idx]
#
#
# # class Parser:
# #     def __init__(self, input_string: str):
# #         self.input_string = input_string
# #
# #     def _validate_helper(self, idx, num_open_paren):
# #         pass
# #
# #     def _validate(self):
# #         return self._validate_helper(0, 0)
# #
# #     def evaluate(self):
# #         if self._validate():
# #             return eval(self.input_string.replace("^", "**"))
# #
# #         raise ValueError("Invalid input!")
#
#
#
