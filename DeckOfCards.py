import random

class DeckOfCards :
    deck = []
    suits = {"D", "C", "H", "S"}
    values = range(2, 15)
    def make (self,deck):
        for suit in self.suits:
            for value in self.values:
                deck.append(f'{value}{suit}')

    def draw(self,deck,jucator,score):
        card = random.choice(deck)
        deck.remove(card)
        jucator.append(card)
        if card[1] == '4':
            score = score+11
        elif '0' <= card[1] <= '9':
            score = score+10
        else:
            score = score+int(card[0])
        return score




class player ():

    hand = []
    nr_of_aces = 0
    cardPhoto = []
    size = 2
    isdealer = False
    score = 0
    def __init__(self):
        self.hand = []
        self.cardPhoto = []
        self.size = 2
        self.isdealer = False
        self.score = 0
        self.nr_of_aces = 0




def last_card_score(player):
    card = player.hand[player.size-1]
    value = 0
    if card[1] == '4':
        value = 11
    elif '0' <= card[1] <= '4':
        value = 10
    else:
        value = int(card[0])

    return value