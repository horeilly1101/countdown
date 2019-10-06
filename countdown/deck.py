
from random import randint


class Deck:
    def __init__(self):
        self._cards = [4] * 13

    def _draw(self):
        num_cards_remaining = sum(self._cards)
        chosen_card = randint(num_cards_remaining)

        count = 0
        for card, num_remaining in enumerate(self._cards):
            count = count + num_remaining
            if count >= chosen_card:
                self._cards[card] = self._cards[card] - 1
                return card

        raise ValueError("The deck is empty!")

    def draw_six_cards(self):
        return [self._draw() for _ in range(6)]
