
class _Card:
    pass


class Deck:
    def __init__(self, cards_remaining=(4,)*13):
        self.cards_remaining = cards_remaining

    def draw(self):
