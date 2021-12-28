class Card:
    cards = {0 : { "name": "Boba",      "action" : "Draw or Play a Card"}
            ,1 : { "name": "Aloe",      "action" : "Draw a Card"}
            ,2 : { "name": "Lychee",    "action" : "Draw a Card"}
            ,3 : { "name": "Pudding",   "action" : "Draw a Card"}
            ,4 : { "name": "Red Bean",  "action" : "Draw a Card"}
            ,5 : { "name": "Taro",      "action"  : "Pair this with milke ot complete this drink set."}
            ,6 : { "name": "Black Tea"}
            ,7 : { "name":"Green Tea"}
            ,8 : { "name":"Milk"}
            ,9 : { "name":"Passion Fruit"}
            ,10 : { "name":"Peach"}
            ,11 : { "name":"Honey Lemon"}
            ,12 : { "name": "Wild Ingredient",      "action" : "Play as any ingredient of your choice. Cannot be a special ingredient. This card is protected from action cards that target a specific type of ingredient."}
            ,13 : { "name": "Sabobatage",           "action" : "Destroy a total of 5 ingredient cards on the table from one or more players. All 5 cards must be declared before a player can play any counter cards"}
            ,14 : { "name": "Lactose Intolerant",   "action" : "Choose a player. They have to trash 1 milk ingredient from their table."}
            ,15 : { "name": "5-Star Review",        "action" : "Play this card and draw 2 cards."}
            ,16 : { "name": "Bobasurance",          "action" : "Place this on any drink set in progress or completed. The set is now protected against an action card one time. When any ingredient from the protected set is targeted, discard the bobasurance card."}
            ,17 : { "name": "Customer Loyalty",     "action" : "Use this to negate another player's action card used against you."}
            ,18 : { "name": "Health Inspector",     "action" : "Choose a player. Choose 1 type of topping OR flavor card on their table. They must trash all of them. This cannot be used against Wild Ingredient."}
            ,19 : { "name": "BOGO",                 "action" : "Pick a random card from a player's hand and put it in your hand. If successful, draw an extra card from the deck."}
            ,20 : { "name": "POS DOWN",             "action" : "Choose a player to skip their upcoming turn."}
            ,21 : { "name": "Straw",                "action" : "Place this onto a completed drink set to keep it safe from others. The set is now unaffected by any action cards."}
            ,22 : { "name": "Sugar and Ice",        "action" : "Steal an ingredient card from another player's table and place it anywhere on your table."}
            ,23 : { "name": "Tea Party",            "action" : "Steal up to 2 tea cards on the table and place them on your table."}
            ,24 : { "name": "Untrained Employee",   "action" : "Choose a player. They choose an incomplete drink set on their table to discard."}}
   
    def __init__(self, id):
        self.name = Card.cards[id]["name"]
        self.description = Card.cards[id]["action"]


