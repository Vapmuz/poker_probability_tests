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
    """class to handle the cards and the game, the class inherited from Deck.
      The class takes as argument the number of people, the number of decks  """
    def __init__(self, num_players, nr_decks):
        """
        instantiate the deck and the Hand
        create a matrix to handle the players hands
        """
        super().__init__(nr_decks)
        self.num_players = num_players
        self.players_hands = [Hand() for _ in range(num_players)]
        self.cards_on_table = Hand()

    def access_hand_class(self, to_test):
        """function used to set up and test the accessibility of
          the Hands using the game asembler"""
        hand_test = Hand()
        hand_test.add_card(to_test)
        return(hand_test.cards)

    def draw_to_player(self, player_index):
        """Add a card to a player's hand given 
        the player index"""
        card = self.deal_card()
        self.players_hands[player_index].add_card(card)

    def draw_all_player(self):
        """
        draw a card for everyone
        """

        for x in (self.players_hands): 
            card =self.deal_card()
            x.add_card(card)

    def display_player_hand(self, player_number):
        """display a specific player hand"""
        hand = self.players_hands[player_number]
        cards= []
        for card in hand.cards:
            cards.append(card.display())
        return cards

    def display_player_hand_in_rank(self, player_number):
        """display a specific player hand using rank"""
        hand = self.players_hands[player_number]
        cards= []
        for card in hand.cards:
            cards.append(card.rank)
        return cards

    def display_player_hand_in_suits(self, player_number):
        """display a specific player hand using rank"""
        hand = self.players_hands[player_number]
        cards= []
        for card in hand.cards:
            cards.append(card.suit)
        return cards

    def display_all_ranks(self):
        """display all the hands in the table"""
        hands = []
        for i in range(self.num_players):
            hands.append(self.display_player_hand_in_rank(i))
        return hands
 
    def display_all_suits(self):
        """display all the hands in the table"""
        hands = []
        for i in range(self.num_players):
            hands.append(self.display_player_hand_in_suits(i))
        return hands
       

    def display_all_hands(self):
        """display all the hands in the table"""
        hands = []
        for i in range(self.num_players):
            hands.append(self.display_player_hand(i))
        return hands
    
    def display_player_ranks(self):
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
    
    
    def display_player_suits(self):
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
    
    def raw_return_player_cards(self, player_index):
        """return the card class of a palyer"""
        cards_player =[]
        for x in self.players_hands[player_index].cards:
            cards_player.append(x)
        return(cards_player)
    
    
    def pop_player(self, number_player):
        """pop a player out of the deck"""
        self.players_hands.pop(number_player)
    
