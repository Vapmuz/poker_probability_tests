"""create a class that assembles a game taking the number of players and a deck of cards
this module must do:
    import the hand module
    make a list  to contain the players' hands, use the module hand to create each hand
    make a list to represent the pool using the hand module
    have a value that represents the number of actions taken in the game, that every time deal card  is called it grows 
    make a function to deal a card to a player from the pool
    make a function to a deal a card to each player 
"""
from hand import Hand
class GameAssembler:
    def __init__(self, num_players, deck):
        """Initialize the game assembler with the number of players and the deck.

        Args:
            num_players: Number of players in the game.
            deck_in_deck: The deck of cards using the Deck class.
        """
        self.num_players = num_players
        self.deck = deck
        self.relative_pool = Hand()
        self.players_hands = [Hand() for _ in range(num_players)]
        self.actions_taken = 0

    def discard_a_card(self):
        """Deal a card from the deck to the absolute pool, removing it from the game and not adding it to any hand."""
        self.deck.deal_card()
        self.actions_taken += 1
   

    def deal_card_relative_pool(self):
        """Deal a card from the deck to the pool.

        Args:
            card_position: Position of the card in the deck to add to the pool.
        """
        self.deck.deal_card()
        self.relative_pool.add_card(self.deck.pool[self.actions_taken])
        self.actions_taken += 1

    def deal_card_to_player(self):
        """Deal a card from the relative pool to each player's hand."""
        for player_hand in self.players_hands:
            self.deck.deal_card()
            player_hand.add_card(self.deck.pool[self.actions_taken]) 
            self.actions_taken += 1