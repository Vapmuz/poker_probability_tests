"""make a unittest for the game assembler module"""
import unittest
from game_assembler import GameAssembler    
import cards as crds


class unitTestGameAssembler(unittest.TestCase):
    """class to test the game assembler module"""
    def test_game_assembler_initialization(self):
        """test the initialization of the game assembler class"""
        game = GameAssembler(4)
        self.assertEqual(game.num_players, 4)
        self.assertEqual(len(game.cards), 104)  # Since it initializes with 2 decks

    def test_access_hand_class(self):
        """test the access to the Hand class through GameAssembler"""
        game = GameAssembler(2)
        card = game.access_hand_class("prova")
        self.assertIsNotNone(card)
        self.assertIn("prova", card)

    def test_access_hand_class_with_dealt_card(self):
        """test the access to the Hand class through GameAssembler with a dealt card"""
        game = GameAssembler(2)
        dealt_card = game.deal_card()
        card = game.access_hand_class(dealt_card)
        self.assertIsNotNone(card)
        self.assertIn(dealt_card, card)
        self.assertEqual(card[0].display(),"Ace of Spades")  # Just to ensure the method works without error
        
    def test_draw_to_player_hand(self):
        """test adding a card to a player's hand"""
        game = GameAssembler(2)
        game.players_hands[0].add_card("prova")
        self.assertEqual(game.players_hands[0].cards[0], "prova")
        game.players_hands[1].add_card(game.deal_card())
        self.assertEqual(game.players_hands[1].cards[0].display(), "Ace of Spades")
        game.draw_to_player(1)
        self.assertEqual(game.players_hands[1].cards[1].display(), "King of Spades")

    def test_draw_card_for_everybody(self):
        """
        draw a card for every hand in the play
        """
        game = GameAssembler(2)
        game.draw_all_player()
        self.assertEqual(game.players_hands[0].cards[0].display(), "Ace of Spades")
        self.assertEqual(game.players_hands[1].cards[0].display(), "King of Spades")
        self.assertEqual(True,True)
    def test_display_hands(self):
        """test for the display hand function"""
        game = GameAssembler(2)
        self.assertEqual(game.display_hands(), [[],[]])
        game.draw_to_player(1)
        self.assertEqual(game.display_hands(), [[],['Ace of Spades']])
        game.draw_all_player()
        self.assertEqual(game.display_hands(),[['King of Spades'], ['Ace of Spades','Queen of Spades']])
        
