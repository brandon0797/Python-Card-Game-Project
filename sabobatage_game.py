from deck import Deck
from player import Player

#4 players, take turns, later figure out how to decide who starts
#start by shuffling a new deck and giving each player 5 cards
#On each turn player draws 2 and can play up to 3, at the end of each turn if player has >7 cards they must discard till =7

deck = Deck()

def players_setup(players : list, amount : int, deck : Deck):
    #Initialize number of players
    for i in range(0, amount):
        players.append(Player(str(i)))
        for j in range(0,5):
            players[i].add_card(deck.draw_card())
    return players

def main():
    players = []
    num_players = 4
    print(len(deck.cards))
    players_setup(players, num_players, deck)
    print(len(deck.cards))
    for i in range(0,len(players)):
        players[i].print_hand()
    
    for j in range(0,len(players)):
        player_turn(players[j])

def player_turn(player : Player):
    #method to use to do all of player's actions
    #parameter is the current player's turn

    plays = 3 #Number of cards they can play
    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())
    player.add_card(deck.draw_card())

    print("Player " + str(player.name) + "'s turn")
    print("Your Hand:")
    player.print_hand()
    for i in range(0,plays):
        while True:
            try:
                play = input("Which card do you want to play? #1-" +str(len(player.hand)) +": ")
                if(int(play) > len(player.hand) or int(play) < 0):
                    print("Invalid Number Choice, please try again")
                    continue
                card = player.play_card(int(play)-1)
                deck.discard_card(card)
            except ValueError:
                print("Invalid Card Selection, please use a number!")
                continue
            else:
                break
        
        if(i < plays - 1):
            print("Next card:")

    print(deck.print_discard())
    return
    
#Card Interactions
#Adding Card IDS to methods to know what each card would call
def target_player():
    #Card IDs - 13, 14, 18, 19, 20, 22, 23, 24
    #cause player to discard cards or set (seperate method with diff parameter?)
    return

def protect_set(set : int):
    #Card IDs - 16, 21
    #maybe implement into player too?
    #Check number of sets player is working on and ask to protect which one
    return

def check_protect(set : int):
    #Card IDs - 13, 14 ,18, 19, 20 ,22, 23, 24
    #check if the targeted set has protection (Straw,Bobasurance)?

    return

def skip_turn():
    #Card IDs - 20
    #change order of the turns?
    return 

if __name__ == "__main__":
    main()