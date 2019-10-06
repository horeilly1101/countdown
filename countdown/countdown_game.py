from countdown.deck import Deck
from countdown.parser import Parser
from countdown.expression import Expression
from countdown.responses import *
from typing import Tuple


class CountdownGame:
    def __init__(self):
        self._deck = Deck()
        self._parser = Parser()

    def _check_validity(self, expression, cards) -> bool:
        pass

    def _compute_goal(self) -> Tuple[Expression, int]:
        pass

    def start(self):
        print(RULES)
        self.play_round(0)

    def play_round(self, round_num):
        cards = self._deck.draw_six_cards()
        goal_expression, goal = self._compute_goal()

        response = input(START_ROUND(round_num, cards, goal))
        expression = self._parser.parse(response)

        if not self._check_validity(expression, cards):
            print(INVALID_INPUT)
            return

        result = expression.evaluate()
        result_message = f"""
        You submitted {expression} = {result}.
        Our solution was {goal_expression} = {result}.
        """
