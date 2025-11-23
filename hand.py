"""
It contains a class that represents a hand of playing cards o the real pool.
the class must do:
    take a card from the pool and add it to the hand"""

class Hand:
    def __init__(self):
        """Initialize an empty hand."""
        self.cards = []

    def add_card(self, card):
        """Add a card to the hand.

        Args:
            pool: The card to be added 
            position: the position in the deck 
        """
        self.cards.append(card)
