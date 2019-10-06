from countdown.deck import Deck
from countdown.parser import Parser
from countdown.expression import Expression
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
        pass

    def play_round(self):
        cards = self._deck.draw_six_cards()
        goal_expression, goal = self._compute_goal()

        user_query = f"""
        Your cards are {[card for card in cards]}.
        Your goal is {goal}.
        
        You may add, subtract, multiply, and divide, but your
        answer MUST be an integer. You don't have to use all
        of the numbers, but you can't use any numbers that haven't
        been given.
        
        Give your solution as an algebraic expression (e.g. 5 * 6 + 9).
        You may use parentheses.
        
        You have 60 seconds.
        
        Your answer:"""
        response = input(user_query)
        expression = self._parser.parse(response)

        if not self._check_validity(expression, cards):
            print("\t\tYour response was invalid! Please try again "
                  "in the next round.")
            return

        result = expression.evaluate()
        result_message = f"""
        You submitted {expression} = {result}.
        Our solution was {goal_expression} = {result}.
        """
