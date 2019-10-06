"""File that contains testing suite for the Countdown game."""
import unittest
from parser import Parser


class TestParser(unittest.TestCase):
    def setUp(self) -> None:
        self.parser = Parser()

    def test_add(self):
        result1 = self.parser.parse("5+5+5+7")
        self.assertEqual(22, result1.evaluate())

        result2 = self.parser.parse("5+7+14")
        self.assertEqual(26, result2.evaluate())

    def test_subtract(self):
        pass

    def test_multiply(self):
        pass

    def test_divide(self):
        pass

    def test_parentheses(self):
        result1 = self.parser.parse("((5+5)+(5+7))")
        self.assertEqual(22, result1.evaluate())

    def test_order_of_operations(self):
        pass
