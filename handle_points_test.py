"""tests for the handle points class"""
import unittest
from handle_points import HandlePoints
from cards import Card

class TestHandlePoints(unittest.TestCase):
    """test the handle points class"""
    def test_init(self):
        """test if the init function of handle points is good"""
        handle_points = HandlePoints([[1],[2],[3,4,5,6,7],[8,9]])
        self.assertEqual(handle_points.pool, [1,2,3,4,5,6,7,8,9])
    
    def test_card_values(self):
        """test if incorrect values and correct ones are handled correctly"""
        handle_points= HandlePoints([[  Card("3","Clubs"),Card("2", "Spades"),Card('Ace', "Spades"),Card('2','Clubs')]])
        handle_points.cards_values()
        self.assertEqual(handle_points.values,{
            "2":2,
            "3":1,
            "4":0,
            "5":0,
            "6":0,
            "7":0,
            "8":0,
            "9":0,
            "10":0,
            "Jack":0,
            "Queen":0,
            "King":0,
            "Ace":1,
            "Hearts":0,
            "Diamonds":0,
            "Clubs":2, 
            "Spades":2
            })

    def test_count_if(self):
        """test the count if function"""
        hp = HandlePoints([[Card("2", "Spades"), Card("2","Clubs"), Card("Ace","Spades")]])
        hp.cards_values()

        card_pair = hp.count_if(2)
        self.assertEqual(card_pair, ['2', 'Spades'])


        #todo:
        card_tris = hp.count_if(3)
        self.assertEqual(card_tris,["3"])

        card_poker = hp.count_if(4)
        self.assertEqual(card_poker,["Jack"])

        card_color = hp.count_if(5)
        self.assertEqual(card_color,["spades"])



    def test_count_high_card(self):
        """test for count_high_card"""
        hp = HandlePoints([[Card("2", "Spades"), Card("3","Clubs"), Card("Ace","Spades")]])
        hp.cards_values()
        hp.count_high_card()
        self.assertEqual(hp.values,{
            "2":1,
            "3":1,
            "4":0,
            "5":0,
            "6":0,
            "7":0,
            "8":0,
            "9":0,
            "10":0,
            "Jack":0,
            "Queen":0,
            "King":0,
            "Ace":1,
            "Hearts":0,
            "Diamonds":0,
            "Clubs":1, 
            "Spades":2
            })
        self.assertEqual(hp.points_d,
            {
            'couple_rank': 0,
            'high_card': 1,
            'lowest_card_straight': 0,
            'tris_card': 0,
            'value': 0
            })



"""
    def test_count_couple(self):
        hp = HandlePoints()

    def test_count_double_couple(self):
       hp = HandlePoints()
 
    def test_count_tris(self):
       hp = HandlePoints()
    
    def test_count_color(self):
       hp = HandlePoints()
   
    def test_count_straight(self):
       hp = HandlePoints()
  
    def test_count_full_house(self):
        hp = HandlePoints()
     
    def test_count_four_of_a_kind(self):
        hp = HandlePoints()
 
    def test_straight_flush(self):
        hp = HandlePoints()
    
    def test_royal_flush(self):
        hp = HandlePoints()"""


        