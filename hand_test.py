"""tests for hand module"""
import unittest
from hand import Hand       
class TestHand(unittest.TestCase):
    def setUp(self):
        """Set up a Hand instance before each test."""
        self.hand = Hand()

    def test_add_card(self):
        """Test adding a card to the hand."""
        card= ('5S')  # Example pool of cards
        self.hand.add_card(card)
        self.assertIn('5S', self.hand.cards)
        self.assertEqual(len(self.hand.cards), 1)

    def test_multiple_add_card(self):
        """Test adding multiple cards to the hand."""
        cards = ['3H', 'KD', '7C']
        for card in cards:
            self.hand.add_card(card)
        self.assertEqual(self.hand.cards, cards)
        self.assertEqual(len(self.hand.cards), 3)
   