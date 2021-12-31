class Card:
    cards = {0 : { 'name': 'Boba',                  'type': 'Topping', 'action': 'Draw or Play a Card'}
            ,1 : { 'name': 'Aloe',                  'type': 'Topping', 'action': 'Draw a Card'}
            ,2 : { 'name': 'Lychee Jelly',          'type': 'Topping', 'action': 'Draw a Card'}
            ,3 : { 'name': 'Pudding',               'type': 'Topping', 'action': 'Draw a Card'}
            ,4 : { 'name': 'Red Bean',              'type': 'Topping', 'action': 'Draw a Card'}
            ,5 : { 'name': 'Taro',                  'type': 'Topping', 'action': 'Pair this with milk to complete this drink set.'}
            ,6 : { 'name': 'Black Tea',             'type': 'Tea', 'action': ''}
            ,7 : { 'name': 'Green Tea',             'type': 'Tea', 'action': ''}
            ,8 : { 'name': 'Milk',                  'type': 'Flavor', 'action': ""}
            ,9 : { 'name': 'Passion Fruit',         'type': 'Flavor', 'action': ""}
            ,10 : { 'name': 'Peach',                'type': 'Flavor', 'action': ""}
            ,11 : { 'name': 'Honey Lemon',          'type': 'Flavor', 'action': ""}
            ,12 : { 'name': 'Wild Ingredient',      'type': 'Action', 'action': "Play as any ingredient of your choice. Cannot be a special ingredient. This card is protected from action cards that target a specific type of ingredient."}
            ,13 : { 'name': 'Sabobatage',           'type': 'Action', 'action': "Destroy a total of 5 ingredient cards on the table from one or more players. All 5 cards must be declared before a player can play any counter cards"}
            ,14 : { 'name': 'Lactose Intolerant',   'type': 'Action', 'action': "Choose a player. They have to trash 1 milk ingredient from their table."}
            ,15 : { 'name': '5-Star Review',        'type': 'Action', 'action': "Play this card and draw 2 cards."}
            ,16 : { 'name': 'Bobasurance',          'type': 'Action', 'action': "Place this on any drink set in progress or completed. The set is now protected against an action card one time. When any ingredient from the protected set is targeted, discard the bobasurance card."}
            ,17 : { 'name': 'Customer Loyalty',     'type': 'Action', 'action': "Use this to negate another player's action card used against you."}
            ,18 : { 'name': 'Health Inspector',     'type': 'Action', 'action': "Choose a player. Choose 1 type of topping OR flavor card on their table. They must trash all of them. This cannot be used against Wild Ingredient."}
            ,19 : { 'name': 'BOGO',                 'type': 'Action', 'action': "Pick a random card from a player's hand and put it in your hand. If successful, draw an extra card from the deck."}
            ,20 : { 'name': 'POS DOWN',             'type': 'Action', 'action': "Choose a player to skip their upcoming turn."}
            ,21 : { 'name': 'Straw',                'type': 'Action', 'action': "Place this onto a completed drink set to keep it safe from others. The set is now unaffected by any action cards."}
            ,22 : { 'name': 'Sugar and Ice',        'type': 'Action', 'action': "Steal an ingredient card from another player's table and place it anywhere on your table."}
            ,23 : { 'name': 'Tea Party',            'type': 'Action', 'action': "Steal up to 2 tea cards on the table and place them on your table."}
            ,24 : { 'name': 'Untrained Employee',   'type': 'Action', 'action': "Choose a player. They choose an incomplete drink set on their table to discard."}}
   
    ##Breakdown of Card Actions##
    # Protect a drink set, complete(Straw) and/or incomplete(Bobasurance)
    # Pick a player, 1 or more
    # Draw and Discard cards
    # Take card from player, combo of draw and discard?
    # Skip chosen player's turn (implement turn system as a list and move them to the end?)
    # Negate action card used against player (probably hardest to figure out)
    
    def __init__(self, id):
        self.name = Card.cards[id]['name']
        self.type = Card.cards[id]['type']
        self.action = Card.cards[id]['action']

    def print_card(self):
        return self.name