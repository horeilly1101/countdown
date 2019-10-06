"""File that contains the testing suite for Parser."""
import unittest
from countdown.parser import Parser


class TestParser(unittest.TestCase):
    """
    Testing Suite for the Parser class.
    """
    def setUp(self) -> None:
        self.parser = Parser()

    def test_add(self):
        result1 = self.parser.parse("5+5+5+7")
        self.assertEqual(22, result1.evaluate())

        result2 = self.parser.parse("5+7+14")
        self.assertEqual(26, result2.evaluate())

    def test_subtract(self):
        result1 = self.parser.parse("9-5")
        self.assertEqual(4, result1.evaluate())

        result2 = self.parser.parse("67-9")
        self.assertEqual(58, result2.evaluate())

    def test_multiply(self):
        result1 = self.parser.parse("5*5*5")
        self.assertEqual(125, result1.evaluate())

        result2 = self.parser.parse("5*14")
        self.assertEqual(70, result2.evaluate())

    def test_divide(self):
        result1 = self.parser.parse("5/5")
        self.assertEqual(1, result1.evaluate())

        result2 = self.parser.parse("14/7")
        self.assertEqual(2, result2.evaluate())

    def test_parentheses(self):
        result1 = self.parser.parse("((5+5)+(5+7))")
        self.assertEqual(22, result1.evaluate())

        result2 = self.parser.parse("(5*7)+9")
        self.assertEqual(44, result2.evaluate())

    def test_order_of_operations(self):
        pass
