"""Script to play the countdown game."""
from countdown.countdown_game import CountdownGame
from countdown.deck import Deck

if __name__ == "__main__":
    # game = CountdownGame()
    # game.start()
    deck = Deck()
    print(deck.draw_six_cards())
