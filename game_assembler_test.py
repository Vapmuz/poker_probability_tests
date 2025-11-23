"""make a unittest for the game assembler module"""
import unittest
from hand import Hand
from card_deck import Deck
from game_assembler import GameAssembler    

class TestGameAssembler(unittest.TestCase):
    """class to test the game assembler module"""
    def setUp(self):
        """Set up a game assembler instance for testing."""
        self.deck = Deck(2)
        self.game_assembler = GameAssembler(num_players=2, deck=self.deck)

    def test_deal_card_relative_pool(self):
        """Test dealing a card to the relative pool.
        test pool size
        test actions taken increment
        test card added to pool is the correct one

        """
        initial_pool_size = len(self.game_assembler.relative_pool.cards)
        self.game_assembler.deal_card_relative_pool()
        self.assertEqual(len(self.game_assembler.relative_pool.cards), initial_pool_size + 1)
        self.assertEqual(self.game_assembler.actions_taken, 1)
        self.assertEqual(self.game_assembler.relative_pool.cards[0], self.deck.pool[0])

    def test_deal_card_to_player(self):
        """Test dealing a card to each player's hand.
        test hand sizes
        test cards added to hands are the correct ones
        """
        initial_hand_sizes = [len(player_hand.cards) for player_hand in self.game_assembler.players_hands]
        self.game_assembler.deal_card_to_player()
        for i, player_hand in enumerate(self.game_assembler.players_hands):
            self.assertEqual(len(player_hand.cards), initial_hand_sizes[i] + 1)
            self.assertEqual(player_hand.cards[0], self.deck.pool[i])
        #test multiple deals
        self.game_assembler.deal_card_to_player()
        for i, player_hand in enumerate(self.game_assembler.players_hands):
            self.assertEqual(len(player_hand.cards), initial_hand_sizes[i] + 2)
            self.assertEqual(player_hand.cards[1], self.deck.pool[i + 2])