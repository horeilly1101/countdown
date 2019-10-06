
from abc import ABC, abstractmethod


class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class Add(Expression):
    def __init__(self, term1: Expression, term2: Expression):
        self.term1 = term1
        self.term2 = term2

    def evaluate(self) -> int:
        return self.term1.evaluate() + self.term2.evaluate()


class Subtract(Expression):
    def __init__(self, term1: Expression, term2: Expression):
        self.term1 = term1
        self.term2 = term2

    def evaluate(self) -> int:
        return self.term1.evaluate() - self.term2.evaluate()


class Multiply(Expression):
    def __init__(self, factor1: Expression, factor2: Expression):
        self.factor1 = factor1
        self.factor2 = factor2

    def evaluate(self) -> int:
        return self.factor1.evaluate() * self.factor2.evaluate()


class Divide(Expression):
    def __init__(self, dividend: Expression, divisor: Expression):
        self.dividend = dividend
        self.divisor = divisor

    def evaluate(self) -> int:
        evaluated_dividend = self.dividend.evaluate()
        evaluated_divisor = self.divisor.evaluate()

        if evaluated_divisor == 0:  # check division by zero
            raise ValueError("Can't divide by zero!")

        if evaluated_dividend % evaluated_divisor != 0:  # make sure division yields an integer
            raise ValueError("All functions must map to the integers!")

        return int(self.dividend.evaluate() / self.divisor.evaluate())


# class Power(Expression):
#     def __init__(self, base: Expression, exponent: Expression):
#         self.base = base
#         self.exponent = exponent
#
#     def evaluate(self) -> int:
#         return self.base.evaluate() ** self.exponent.evaluate()
