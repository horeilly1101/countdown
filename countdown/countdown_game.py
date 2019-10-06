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

    def end(self):
        print(END_GAME)

    def play_round(self, round_num):
        # initialize the game state for the round
        cards = self._deck.draw_six_cards()
        goal_expression, goal = self._compute_goal()

        # get the user's answer
        response = input(START_ROUND(round_num, cards, goal))
        expression = self._parser.parse(response)

        # check validity
        if not self._check_validity(expression, cards):
            print(INVALID_INPUT)
            return

        # figure out whether or not the answer was correct
        result = expression.evaluate()
        if result == goal:
            print(CORRECT_ANSWER(expression, result))
        else:
            print(INCORRECT_ANSWER(expression, result, goal_expression, goal))

        # stop playing after 5 rounds, or when the user wants to quit
        if round_num < 4:
            keep_playing = input(CONTINUE_PLAYING)
            if keep_playing.strip() == "y":
                self.play_round(round_num + 1)

        self.end()
