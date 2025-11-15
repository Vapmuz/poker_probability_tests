"""
File for the card_deck class.
This module includes:
- A class to represent a standard or multiple standard decks of playing cards using the module cards.py.
- A method to shuffle the deck created.
- A method to deal a card from the deck that goes in the self.pool list.
- A method to remove a specific card from the deck.
"""

from cards import Card
import random


class Deck:
    """Class to represent a standard or multiple standard decks of playing cards."""

    def __init__(self, num_decks):
        """Initialize the deck with the specified number of standard decks."""
        self.cards = []
        for _ in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    self.cards.append(Card(rank, suit))
        self.pool = []

    def shuffle(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal a card from the deck and add it to the pool. Pop the card from the deck and append to the pool."""
        if self.cards:
            card = self.cards.pop()
            self.pool.append(card)
            return card
        else:
            return None

    def remove_card(self, rank, suit):
        """Remove a specific card from the deck given its rank and suit. Then add it to the pool."""
        for card in self.cards:
            if card.rank == rank and card.suit == suit:
                self.cards.remove(card)
                self.pool.append(card)
                return
        return
