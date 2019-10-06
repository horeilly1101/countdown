from countdown.deck import Deck
from countdown.parser import Parser
from countdown.expression import *
from countdown.random_expression_generator import RandomExpressionGenerator
from countdown.responses import *
import countdown.utils as utils
from typing import Tuple, List


class CountdownGame:
    def __init__(self):
        self._deck = Deck()
        self._parser = Parser()
        self._generator = RandomExpressionGenerator()

    def _check_validity(self, expression: Expression, cards: List[int]) -> bool:
        # we want to check whether the (sorted) list of numbers in the
        # expression is a subsequence of the (sorted) cards
        sorted_cards = sorted(cards)
        sorted_numbers = sorted(expression.get_numbers())

        return utils.is_valid_subsequence(sorted_cards, sorted_numbers)

    def _compute_goal(self, cards) -> Tuple[Expression, int]:
        # randomly generate an expression with the given cards
        expr = self._generator.generate_expression(cards)
        return expr, expr.evaluate()

    def start(self):
        print(RULES)
        self._play_round(1)

    def _play_round(self, round_num):
        # initialize the game state for the round
        cards = self._deck.draw_six_cards()
        goal_expression, goal = self._compute_goal(cards)

        # get the user's answer
        response = input(START_ROUND(round_num, cards, goal))
        expression = self._parser.parse(response)

        # check validity
        if not self._check_validity(expression, cards):
            print(INVALID_INPUT)
            self._move_to_next_round(round_num + 1)

        # figure out whether or not the answer was correct
        result = expression.evaluate()
        if result == goal:
            print(CORRECT_ANSWER(expression, result))
        else:
            print(INCORRECT_ANSWER(expression, result, goal_expression, goal))

        self._move_to_next_round(round_num + 1)

    def _move_to_next_round(self, round_num):
        # stop playing after 5 rounds, or when the user wants to quit
        if round_num < 5:
            keep_playing = input(CONTINUE_PLAYING)
            if keep_playing.strip() == "y":
                self._play_round(round_num + 1)
            else:
                self.end()
        else:
            self.end()

    def end(self):
        print(END_GAME)
