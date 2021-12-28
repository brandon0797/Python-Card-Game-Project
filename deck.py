from random import shuffle
from card import Card

# 110 Total Cards
# 24 Toppings: 8 Boba, 3 Aloe, 3 Lychee, 3 Pudding, 3 Red Bean, 4 Taro
# 24 Tea : 12 Black, 12 Grean
# 24 Flavors : 12 Milk, 4 Passion Fruit, 4 Peach, 4 Honey Lemon
# 3 Wild Ingredients
# 35 Actions : 2 Sabobatage, 2 Lactose Intolerant, 5 5-Star Reviews, 3 Bobasurance, 5 Customer Loyalty
#  2 Health Inspector, 3 BOGO, 2 POS Down, 3 Straw, 3 Sugar and Ice, 3 Tea Party, 2 Untrained Employee

class Deck:
    def __init__(self):
        self.cards = []
        self.discard = [] # Discard pile to reshuffle when empty

        for i in range(0,8):
            self.cards.append(IngredientCard("Boba", ))
        
        shuffle(self.cards)

    def draw_card(self):
        #If deck is empty, move discard pile to deck and reshuffle and draw card.
        if len(self.cards) == 0:
            self.cards = self.discard[:]
            self.discard.clear()
            shuffle(self.cards)
            return self.cards.pop()

        return self.cards.pop()
    
    def discard_card(self):
        self.discard.append()


def main():
    action = ActionCard("Sabobatage")
    print(action.description)

if __name__ == "__main__":
    main()