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
        handle_points= HandlePoints([[Card('Ace', "Spades"),Card('2','Clubs')]])
        handle_points.cards_values()
        self.assertEqual(handle_points.values,{
            "2":1,
            "3":0,
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
            "Spades":1
            })
        