"""Test the cases for the Card and Deck classes."""

import unittest
from cards import Card


class TestCard(unittest.TestCase):
    """Test the functions in the Card class."""

    def test_display_card_true(self):
        """Test the display method for a valid card."""
        card = Card("Ace", "Spades")
        self.assertTrue(card.card_exists())
        self.assertEqual(card.display(), "Ace of Spades")

    def test_display_card_false(self):
        """Test the display method for an invalid card."""
        card = Card("11", "Stars")
        self.assertFalse(card.card_exists())
        self.assertEqual(card.display(), "Invalid card")

    def test_card_exists(self):
        """Test the card_exists method."""
        card1 = Card("10", "Hearts")
        card2 = Card("Joker", "None")
        self.assertTrue(card1.card_exists())
        self.assertFalse(card2.card_exists())
