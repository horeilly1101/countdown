
from abc import ABC, abstractmethod


class Expression(ABC):
    """
    An Expression is a recursive, compositional data structure that represents
    a mathematical expression.
    """
    def __eq__(self, other):
        """
        Overridden equals method. We will define two expressions to be "equal"
        if they evaluate to the same integer.

        :param other: input to be checked for equality
        :return: whether or not the two objects are equal
        """
        if not isinstance(other, Expression):
            return False

        return self.evaluate() == other.evaluate()

    @abstractmethod
    def evaluate(self) -> int:
        """
        Evaluate the expression, and output an integer. For example, evaluating
        4 + 5 * 6 would output 34.

        :return: integer result
        """


class Add(Expression):
    """
    An Expression that represents addition. More precisely, an Add
    is the sum of two terms.
    """
    def __init__(self, term1: Expression, term2: Expression):
        self.term1 = term1
        self.term2 = term2

    def __repr__(self) -> str:
        return f"Add({self.term1}, {self.term2})"

    def __str__(self) -> str:
        return f"({self.term1} + {self.term2})"

    def evaluate(self) -> int:
        return self.term1.evaluate() + self.term2.evaluate()


class Subtract(Expression):
    """
    An Expression that represents subtraction. More precisely, a Subtract
    is the difference between two terms.
    """
    def __init__(self, term1: Expression, term2: Expression):
        self.term1 = term1
        self.term2 = term2

    def __repr__(self) -> str:
        return f"Subtract({self.term1}, {self.term2})"

    def __str__(self) -> str:
        return f"({self.term1} - {self.term2})"

    def evaluate(self) -> int:
        return self.term1.evaluate() - self.term2.evaluate()


class Multiply(Expression):
    """
    An Expression that represents multiplication. More precisely, a Multiply
    is the product of two factors.
    """
    def __init__(self, factor1: Expression, factor2: Expression):
        self.factor1 = factor1
        self.factor2 = factor2

    def __repr__(self) -> str:
        return f"Multiply({self.factor1}, {self.factor2})"

    def __str__(self) -> str:
        return f"({self.factor1} * {self.factor2})"

    def evaluate(self) -> int:
        return self.factor1.evaluate() * self.factor2.evaluate()


class Divide(Expression):
    """
    An Expression that represents division. More precisely, a Divide
    is the quotient of two factors.
    """
    def __init__(self, dividend: Expression, divisor: Expression):
        self.dividend = dividend
        self.divisor = divisor

    def __repr__(self) -> str:
        return f"Divide({self.dividend}, {self.divisor})"

    def __str__(self) -> str:
        return f"({self.dividend} / {self.divisor})"

    def evaluate(self) -> int:
        # memoize evaluations
        evaluated_dividend = self.dividend.evaluate()
        evaluated_divisor = self.divisor.evaluate()

        if evaluated_divisor == 0:  # check division by zero
            raise ValueError("Can't divide by zero!")

        if evaluated_dividend % evaluated_divisor != 0:  # make sure division yields an integer
            raise ValueError("All functions must map to the integers!")

        return int(self.dividend.evaluate() / self.divisor.evaluate())


class Number(Expression):
    """
    An Expression that represents an integer. A Number is pretty much
    a wrapper around an int, and it functions as our base case
    when evaluating Expressions.
    """
    def __init__(self, num: int):
        self.num = num

    def __repr__(self) -> str:
        return f"Number({self.num})"

    def __str__(self) -> str:
        return str(self.num)

    def evaluate(self) -> int:
        return self.num
