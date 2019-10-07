"""File that contains the CountdownGame."""
from typing import Tuple, List

from lark.exceptions import LarkError

from countdown.deck import Deck
from countdown.parser import Parser
from countdown.expression import Expression
from countdown.random_expression_generator import RandomExpressionGenerator
import countdown.display_text as display_text
import countdown.utils as utils


class CountdownGame:
    """
    Class that represents the game state.
    """
    def __init__(self):
        self._deck = Deck()
        self._parser = Parser()
        self._generator = RandomExpressionGenerator()

    def _check_validity(self, expression: Expression, cards: List[int]) -> bool:
        """
        Check that only valid numbers have been used in the input expression.

        :param expression: input expression
        :param cards: list of cards
        :return: whether or not the input expression only uses the cards given.
        """
        # we want to check whether the (sorted) list of numbers in the
        # expression is a subsequence of the (sorted) cards
        sorted_cards = sorted(cards)
        sorted_numbers = sorted(expression.get_numbers())

        return utils.is_valid_subsequence(sorted_cards, sorted_numbers)

    def _compute_goal(self, cards) -> Tuple[Expression, int]:
        """
        Compute the goal for each round.

        :param cards: list of cards for the round
        :return: the goal expression and evaluation in a tuple
        """
        # randomly generate an expression with the given cards
        expr = self._generator.generate_expression(cards)
        return expr, expr.evaluate()

    def start(self) -> None:
        """
        Start the game in the main thread.
        """
        input(display_text.RULES)
        self._play_round(1)

    def _play_round(self, round_num) -> None:
        """
        Play a round of the countdown game.
        :param round_num: the number of the round (e.g. 4)
        """
        # initialize the game state for the round
        cards = self._deck.draw_six_cards()
        goal_expression, goal = self._compute_goal(cards)

        # get the user's answer
        round_text = display_text.START_ROUND(round_num, cards, goal)
        response = input(round_text)

        # parse the input expression
        try:
            expression = self._parser.parse(response)
        except LarkError:
            print(display_text.PARSE_ERROR)
            self._move_to_next_round(round_num)
            return

        # check validity
        if not self._check_validity(expression, cards):
            print(display_text.INVALID_NUMBERS_ERROR)
            self._move_to_next_round(round_num)
            return

        # evaluate the input expression
        try:
            result = expression.evaluate()
        except ValueError:
            print(display_text.EVALUATION_ERROR)
            self._move_to_next_round(round_num)
            return

        # figure out whether or not the answer was correct
        if result == goal:
            print(display_text.CORRECT_ANSWER(expression, result))
        else:
            print(display_text.INCORRECT_ANSWER(expression, result, goal_expression, goal))

        self._move_to_next_round(round_num)

    def _move_to_next_round(self, next_round_num) -> None:
        """
        Move to the next round, if fewer than 5 rounds have been played, and the
        user wants to.

        :param next_round_num: the number of the next round
        """
        # stop playing after 5 rounds, or when the user wants to quit
        if next_round_num < 5:
            keep_playing = input(display_text.CONTINUE_PLAYING)
            if keep_playing.strip() == "y":
                self._play_round(next_round_num + 1)
            else:
                self.end()
        else:
            self.end()

    def end(self) -> None:
        """
        End the game.
        """
        print(display_text.END_GAME)
