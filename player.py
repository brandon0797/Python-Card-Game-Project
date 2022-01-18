from card import Card

class Player:
    #Has a hand of drawn cards, Max of 7 cards at end of turn
    #Table has Drink sets to add to
    #Up to 7 inprogress drink sets
    def __init__(self, name : str):
        self.name = name
        self.hand = []
        self.table = {0 : {'Topping': '', 'Tea': '', 'Flavor': ''}
                    , 1 : {'Topping': '', 'Tea': '', 'Flavor': ''}
                    , 2 : {'Topping': '', 'Tea': '', 'Flavor': ''}
                    , 3 : {'Topping': '', 'Tea': '', 'Flavor': ''}
                    , 4 : {'Topping': '', 'Tea': '', 'Flavor': ''}
                    , 5 : {'Topping': '', 'Tea': '', 'Flavor': ''}
                    , 6 : {'Topping': '', 'Tea': '', 'Flavor': ''}}
        
    def add_card(self, card : Card):
        for i in range(0, len(Card.cards)):
            if Card.cards[i]['name'] == card:
                self.hand.append(Card(i))
                return

    def play_card(self, select, table_slot : int):
        #select: index for the card picked to be played
        #table slot: index in table to place card
        card = self.hand.pop(select)
        card_type = card.type
        keys = list(self.table[table_slot].keys())

        for i in range(0,len(keys)):
            if keys[i] == card_type:
                if self.table[table_slot][card_type] == '':
                    self.table[table_slot][card_type] = card.name
                    print(card.name + ' Card placed')
                    if card.type == 'Topping' & card.name != 'Boba':
                        print("Draw a card")
                    else:
                        print("Draw or Play a Card")
                    return
                else:
                    print('There is already a '+ card_type +' card placed here.')
                    return    
    
    def play_card(self, select): # returns the action to call in game
        card = self.hand.pop(select)
        return card

    #Test Print methods
    def print_table(self):
        print(self.table)    

    def print_hand(self):
        hand_list = []
        for i in range(0,len(self.hand)):
            hand_list.append(self.hand[i].name)
        print(hand_list)
    
    def print_card_in_hand(self, index):
        print('The Card in index ' + str(index) + ' is ' + self.hand[index].name)
