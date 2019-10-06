from random import randint, choice

from countdown.expression import Add, Multiply, Divide, Subtract, Expression, Number


class RandomExpressionGenerator:
    """
    Class that randomly constructs Expression objects, given a
    list of numbers.
    """
    _OPERATORS = [
        Add,
        Multiply,
        Divide,
        Subtract
    ]

    _OPERATORS_WITHOUT_DIVISION = [
        Add,
        Multiply,
        Subtract
    ]

    def _generate_expression_helper(self, numbers) -> Expression:
        # base case, create a number
        if len(numbers) == 1:
            return Number(numbers[0])

        # we want to successively divide the cards in halves, and
        # then build them up as Expressions
        rand_idx = randint(1, len(numbers) - 1)
        expr1 = self._generate_expression_helper(numbers[:rand_idx])
        expr2 = self._generate_expression_helper(numbers[rand_idx:])

        # check if division is valid
        if expr1.evaluate() % expr2.evaluate() == 0:
            op = choice(self._OPERATORS)
            return op(expr1, expr2)

        op = choice(self._OPERATORS_WITHOUT_DIVISION)
        return op(expr1, expr2)

    def generate_expression(self, numbers) -> Expression:
        return self._generate_expression_helper(numbers)
