"""File that contains the Deck class."""
from random import randint
from typing import List


class Deck:
    """
    Class that represents a deck of cards. A card is represented
    as an integer from 1 to 13.
    """
    def __init__(self):
        self._cards = [4] * 13

    def _draw(self) -> int:
        """
        Draw a card from the deck. The returned card will be
        removed from the deck.

        :return: an integer, that represents a card
        """
        num_cards_remaining = sum(self._cards)

        # we want to choose our card uniformly at random
        chosen_card = randint(0, num_cards_remaining - 1)

        count = 0
        for card, num_remaining in enumerate(self._cards):
            count = count + num_remaining
            if count >= chosen_card:
                self._cards[card] = self._cards[card] - 1

                # account for the fact that lists index at 0
                return card + 1

        raise ValueError("The deck is empty!")

    def draw_six_cards(self) -> List[int]:
        """
        Draw six cards from the deck, and return them in a list.
        :return:
        """
        return [self._draw() for _ in range(6)]
