"""create a class that assembles a game taking the number of players and a deck of cards
this module must do:
    make a list  to contain the players' hands, use the module hand to create each hand
    make a list to represent the pool using the hand module
    have a value that represents the number of actions taken in the game, that every time deal card  is called it grows 
    make a function to deal a card to a player from the pool
    make a function to a deal a card to each player 
"""
from hand import Hand
from card_deck import Deck
class GameAssembler(Deck):
    """class to handle the cards and the game, the class inherited from Deck"""
    def __init__(self, num_players):
        """
        instantiate the deck and the Hand
        create a matrix to handle the players hands
        """
        super().__init__(2)
        self.num_players = num_players
        self.players_hands = [Hand() for _ in range(num_players)]
        self.discarded_cards = Hand()

    def access_hand_class(self, to_test):
        """function used to set up and test the accessibility of the Hands using the game asembler"""
        hand_test = Hand()
        hand_test.add_card(to_test)
        return(hand_test.cards)

    def draw_to_player(self, player_index):
        """Add a card to a player's hand given the player index and the card"""
        card = self.deal_card()
        self.players_hands[player_index].add_card(card)

    def draw_all_player(self):
        """
        draw a card for everyone
        """

        for x in (self.players_hands): 
            card =self.deal_card()
            x.add_card(card)

    def display_hands(self):
        """
        display all the hands
            it returns a list containing strings that are easily human readable"""
        hands =[]
        a=0
        for _ in self.players_hands:
            cards = [card.display() for card in self.players_hands[a].cards]
            a=+1
            hands.append(cards)
        return hands
    
    def display_ranks(self):
        """
        Display all the people's cards ranks
            it returns a list containing strings that are easily human-readable
        """
        hands =[]
        a=0
        for _ in self.players_hands:
            ranks = [card.rank for card in self.players_hands[a].cards]
            a=+1
            hands.append(ranks)
        return hands
    
    
    def display_suits(self):
        """
        Display all the people's cards ranks
            it returns a list containing strings that are easily human-readable
        """
        hands =[]
        a=0
        for _ in self.players_hands:
            suits = [card.suit for card in self.players_hands[a].cards] 
            a=+1
            hands.append(suits)
        return hands
    
