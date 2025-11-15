"""
Class to represent a card of a standard deck of playing cards.
The class must include:
- Attributes for rank and suit
- A method to display the card as a string (e.g., "Ace of Spades")
- A method to check if the card exists
"""


class Card:
    """create a card of a standard deck of playing cards given rank and suit. The number and the ranks are string elements"""

    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self, rank, suit):
        """Initialize the card with rank and suit. It is to notice that the usage of a method to check if the card exists was useful to prevent the creation of invalid cards."""
        if rank in Card.RANKS and suit in Card.SUITS:
            self.rank = rank
            self.suit = suit
            self.exists = True
        else:
            self.rank = None
            self.suit = None
            self.exists = False

    def display(self):
        """Return a string representation of the card."""
        if self.exists:
            return f"{self.rank} of {self.suit}"
        else:
            return "Invalid card"

    def card_exists(self):
        """Check if the card exists in a standard deck."""
        return self.exists
