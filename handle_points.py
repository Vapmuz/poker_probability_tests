"""
Class to handle the poker points
    it shoukd take the cards from the pool and from a player 
    to calculate a rating of the game (from 1 to 10) to 
    assign for then winning   
"""


class HandlePoints():
    """a class to handle the points,
        takes a list of values as argument. 
        Expects it to be a Card class """
        
    def __init__(self, cards):
        self.values = {
            "2":0,
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
            "Ace":0,
            "Hearts":0,
            "Diamonds":0,
            "Clubs":0, 
            "Spades":0
            }
        self.pool= sum(cards, [])

    def cards_values(self):
        """if a keyword matches the dictionary 
        then increment the values of one"""
        for x in self.pool:
            if x.rank in self.values:
                self.values[x.rank] += 1
            if x.suit in self.values:
                self.values[x.suit] += 1  
            else:
                raise ValueError ("putted an unexpected value in the counting method")


        
        

