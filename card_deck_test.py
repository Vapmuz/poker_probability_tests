"""Test the cases for the Deck class."""
import unittest
from card_deck import Deck  

class TestDeck(unittest.TestCase):
    """Test the functions in the Deck class."""
    def test_deck_initialization(self):
        """Test deck initialization with one standard deck."""
        deck = Deck(1)
        deck2 = Deck(2)
        self.assertEqual(len(deck.cards), 52)
        self.assertEqual(len(deck.pool), 0)
        self.assertEqual(len(deck2.cards), 104)
        self.assertEqual(len(deck2.pool), 0)

    def test_shuffle_deck(self):
        """Test shuffling the deck."""
        deck = Deck(1)
        original_order = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_order)

    def test_deal_card(self):
        """Test dealing a card from the deck."""
        deck = Deck(1)
        initial_deck_size = len(deck.cards)
        dealt_card = deck.deal_card()
        self.assertIsNotNone(dealt_card)
        self.assertEqual(len(deck.cards), initial_deck_size - 1)
        self.assertIn(dealt_card, deck.pool)

    def test_remove_card(self):
        """Test removing a specific card from the deck."""
        deck = Deck(1)
        deck.remove_card('Ace', 'Spades')
        for card in deck.cards:
            self.assertFalse(card.rank == 'Ace' and card.suit == 'Spades')
        if not any(card.rank == 'Ace' and card.suit == 'Spades' for card in deck.pool):
            self.fail("Removed card not found in pool")

    def test_remove_nonexistent_card(self):
        """Test removing a card that does not exist in the deck."""
        deck = Deck(1)

        for card in deck.cards:
            self.assertFalse(card.rank == 'Ace' and card.suit == 'None')
    
    def test_out_of_range(self):
        """test if the deck raises arn error when asked for too many cards"""
        deck = Deck(1)
        for _ in range(52):
            deck.deal_card()
        with self.assertRaises(IndexError):
            deck.deal_card()