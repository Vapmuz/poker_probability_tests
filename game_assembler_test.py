"""make a unittest for the game assembler module"""
import unittest
from game_assembler import GameAssembler    



class TestGameAssembler(unittest.TestCase):
    """class to test the game assembler module"""
    def test_game_assembler_initialization(self):
        """test the initialization of the game assembler class"""
        game = GameAssembler(4, 2)
        self.assertEqual(game.num_players, 4)
        self.assertEqual(len(game.cards), 104)  # Since it initializes with 2 decks

    def test_access_hand_class(self):
        """test the access to the Hand class through GameAssembler"""
        game = GameAssembler(2,1)
        card = game.access_hand_class("prova")
        self.assertIsNotNone(card)
        self.assertIn("prova", card)

    def test_access_hand_class_with_dealt_card(self):
        """test the access to the Hand class through GameAssembler with a dealt card"""
        game = GameAssembler(2,1)
        dealt_card = game.deal_card()
        card = game.access_hand_class(dealt_card)
        self.assertIsNotNone(card)
        self.assertIn(dealt_card, card)
        self.assertEqual(card[0].display(),"Ace of Spades")  # Just to ensure the method works without error
        
    def test_draw_to_player_hand(self):
        """test adding a card to a player's hand"""
        game = GameAssembler(2,1)
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
        game = GameAssembler(2,1)
        game.draw_all_player()
        self.assertEqual(game.players_hands[0].cards[0].display(), "Ace of Spades")
        self.assertEqual(game.players_hands[1].cards[0].display(), "King of Spades")
        self.assertEqual(True,True)

    def test_display_player_ranks(self):
        """test for the  display_player_ranks function"""
        game = GameAssembler(2,1)
        self.assertEqual(game.display_player_ranks(), [[],[]])
        game.draw_to_player(1)
        self.assertEqual(game.display_player_ranks(), [[],['Ace']])
        game.draw_all_player()
        self.assertEqual(game.display_player_ranks(),[['King'], ['Ace','Queen']])
 
    def test_display_player_suits(self):
        """test for the display suit function"""
        game = GameAssembler(2,1)
        self.assertEqual(game.display_player_suits(), [[],[]])
        game.draw_to_player(1)
        self.assertEqual(game.display_player_suits(), [[],['Spades']])
        game.draw_all_player()
        self.assertEqual(game.display_player_suits(),[['Spades'], ['Spades','Spades']])

    def test_display_player_hand_in_ranks(self):
        """test the display card using ranks method"""
        game = GameAssembler(3,1)
        for _ in range(13):
            game.draw_to_player(0)
        cards = game.display_player_hand_in_rank(0)
        self.assertEqual(cards, ['Ace', 
                                 "King", 
                                 "Queen", 
                                 "Jack", 
                                 "10", 
                                 "9", 
                                 "8", 
                                 "7", 
                                 "6", 
                                 "5", 
                                 "4", 
                                 "3", 
                                 "2", ])

    def test_display_player_hand_in_suits(self):
        """test the display card using suits method"""
        game = GameAssembler(3,1)
        for _ in range(4):
            game.draw_to_player(0)
        cards = game.display_player_hand_in_suits(0)
        self.assertEqual(cards, ["Spades",
                                  "Spades", 
                                  "Spades", 
                                  "Spades"])


    def test_display_a_player_hand(self):
        "test the display hand of a player"

        game =GameAssembler(5,1)
        game.draw_to_player(0)
        cards = game.display_player_hand(0)
        self.assertEqual(cards, ["Ace of Spades"])
        game.draw_to_player(0)
        game.draw_to_player(0)
        cards = game.display_player_hand(0)
        self.assertEqual(cards, ["Ace of Spades","King of Spades","Queen of Spades"])


    def test_pop_player(self):
        """test the pop_player function"""
        game = GameAssembler(2,1)
        game.draw_all_player()
        self.assertEqual(game.players_hands[0].cards[0].display(), "Ace of Spades")
        self.assertEqual(game.players_hands[1].cards[0].display(), "King of Spades")
        game.pop_player(0) #remove player one that removes the ace of spades
        self.assertEqual(game.display_player_hand(0),["King of Spades"])


                                  

    def test_display_all_hands(self):
        """test all player hands"""
        game = GameAssembler(3,1)

        for i in range(3):
            game.draw_all_player()

        self.assertEqual(game.display_all_hands(), [['Ace of Spades', 'Jack of Spades', '8 of Spades'],
                                                    ['King of Spades', '10 of Spades', '7 of Spades'],
                                                    ['Queen of Spades', '9 of Spades', '6 of Spades']])
 
    def test_display_all_hands_in_ranks(self):
        """test all player hands"""
        game = GameAssembler(3,1)
        for i in range(3):
            game.draw_all_player()
        self.assertEqual(game.display_all_ranks(), 
            [['Ace', 'Jack', '8'],
            ['King', '10', '7'], 
            ['Queen', '9', '6']])
        
    def test_display_all_hands_in_suits(self):
        """test all player hands"""
        game = GameAssembler(3,1)
        for i in range(3):
            game.draw_all_player()
        self.assertEqual(game.display_all_suits(), [
            ['Spades', 'Spades', 'Spades'],
            ['Spades', 'Spades', 'Spades'],
            ['Spades', 'Spades', 'Spades']])
        
    def test_raw_return_player_cards(self):
        """test the card taking method"""
        game = GameAssembler(3,1)
        game.draw_to_player(0)
        card= game.raw_return_player_cards(0)
        self.assertEqual(card[0].rank, 'Ace')
        self.assertEqual(card[0].suit, "Spades")
     