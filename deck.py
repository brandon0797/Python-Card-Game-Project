from random import shuffle
from card import Card
from player import Player

# 110 Total Cards
# 24 Toppings: 8 Boba, 3 Aloe, 3 Lychee, 3 Pudding, 3 Red Bean, 4 Taro
# 24 Tea : 12 Black, 12 Grean
# 24 Flavors : 12 Milk, 4 Passion Fruit, 4 Peach, 4 Honey Lemon
# 3 Wild Ingredients
# 35 Actions : 2 Sabobatage, 2 Lactose Intolerant, 5 5-Star Reviews, 3 Bobasurance, 5 Customer Loyalty
#  2 Health Inspector, 3 BOGO, 2 POS Down, 3 Straw, 3 Sugar and Ice, 3 Tea Party, 2 Untrained Employee

class Deck:
    #array to generate correct amount of each card
    card_amounts = [8,3,3,3,3,4,12,12,12,4,4,4,3,2,2,5,3,5,2,3,2,3,3,3,2]
    def __init__(self): 
        
        self.cards = []
        self.discard = [] # Discard pile to reshuffle when empty

        for i in range(0,25):
            for j in range(0,Deck.card_amounts[i]):
                self.cards.append(Card(i))
        
        shuffle(self.cards)

    def draw_card(self):
        #If deck is empty, move discard pile to deck and reshuffle and draw card.
        if len(self.cards) == 0:
            self.cards = self.discard[:]
            self.discard.clear()
            shuffle(self.cards)
            card = self.cards.pop()
            return (card.name)

        card = self.cards.pop()
        return (card.name)
    
    def discard_card(self, card):
        self.discard.append(card)

    #Test methods to show the deck is created correctly
    def print_deck(self):
        print(len(self.cards))
        for i in range(0,len(self.cards)):
            #print(str(i) + ": " + self.cards[i].name)
            print(self.cards[i].name)
    
    def print_actions(self):
        print(len(self.cards))
        for i in range(0,len(self.cards)):
            print(str(i) + ": " + self.cards[i].action)

def main():
    deck = Deck()
    #deck.print_deck()
    player = Player()
    player.add_card(deck.draw_card())
    player.print_card_in_hand(0)
    player.play_card(0,1)
    player.print_table()

if __name__ == "__main__":
    main()