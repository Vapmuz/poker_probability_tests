"""
Class to handle the poker points

    it shoukd take the cards from the pool and from a player's hand

    calculate the rating of a player's game (from 1 to 10)
    
    it should return a dictionary containing every useful data to decide the winner
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
        self.number_cards_conversion={
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "10":10,
            "Jack":11,
            "Queen":12,
            "King":13,
            "Ace":1,           
        }
        self.pool= sum(cards, [])
        self.points_d = {'value':0, 'high_card':0 ,"couple_rank":0,"tris_card":0, "lowest_card_straight":0,}
 
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

    def count_high_card(self):
        """
        count the highest card of the deck, modify the points_d
            take the first 13 elements in the self.points_d (the cards ranks)
                if there are cards of that type then check if the high card is lower
                if ace (the value is one) high card =1 high card is = 1

        """
        for key, value in list(self.values.items())[:13]: 
            if value>0: 
                value_high_card =self.points_d["high_card"]
                value_card = self.number_cards_conversion[key]
                if value_card > value_high_card:
                    if value_high_card != 1:
                        self.points_d["high_card"] = value_card
                if value_card ==1:
                    self.points_d["high_card"] = value_card  

    def count_if(self, number):
        """
        method to count if there are ranks or suits that have the specified number 
         
        :param self: self 
        :param number: select if couple, tris, poker, 5 cards ...
        
        how:
        
        return: the ranks or the suits in a list that have the desired amount 
        """


        card_type = []
        for key , value in list(self.values.items()):
            if value == number:
                card_type.append(key)
        return(card_type)



    

            
