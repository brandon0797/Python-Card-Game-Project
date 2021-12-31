from deck import Deck
from player import Player

#4 players, take turns, later figure out how to decide who starts
#start by shuffling a new deck and giving each player 5 cards
#On each turn player draws 2 and can play up to 3, at the end of each turn if player has >7 cards they must discard till =7

def players_setup(players : list, amount : int, deck : Deck):
    #Initialize number of players
    for i in range(0, amount):
        players.append(Player(str(i)))
        for j in range(0,5):
            players[i].add_card(deck.draw_card())
    return players

def main():
    deck = Deck()
    players = []
    num_players = 4
    print(len(deck.cards))
    players_setup(players, num_players, deck)
    print(len(deck.cards))
    
    for i in range(0,len(players)):
        players[i].print_hand()
    
#Card Interactions
def target_player():
    #cause player to discard cards
    return

def protect_set():
    #maybe implement into player too?
    return

def check_protect():
    #check if the targeted set has protection (Straw,Bobasurance)?
    return

def skip_turn():
    #change order of the turns?
    return

if __name__ == "__main__":
    main()