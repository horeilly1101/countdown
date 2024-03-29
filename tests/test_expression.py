"""File that contains the test suite for our Expression."""
import unittest
from countdown.expression import *


class TestExpression(unittest.TestCase):
    """Test suite for our Expressions."""
    def test_evaluate(self):
        expr1 = Add(Number(3), Add(Number(9), Number(7)))
        self.assertEqual(19, expr1.evaluate())

    def test_get_numbers(self):
        expr1 = Add(Multiply(Number(5), Number(7)), Number(8))
        self.assertEqual([5, 7, 8], sorted(expr1.get_numbers()))
