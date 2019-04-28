import re
from Card import *
from random import shuffle

class Deck():

    def __init__(self):
        self.cards = []

    def shuffleCards(self):

        p = re.compile("([\w]+\s[\w]+\s[\w]+),([\d]+)")

        with open('cards.txt') as f:
            data = f.readlines()

        for line in data:
            found = p.search(line)
            self.cards.append(Card(found.group(1), found.group(2)))

        shuffle(self.cards)

    def getCards(self):
        return self.cards

    def dealCard(self):
        return self.cards.pop(0)

    def remainingCards(self):
        return len(self.cards)
