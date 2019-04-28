import random
from Card import *

class Hand():

    def __init__(self, name, funds):
        self.name = name
        self.funds = funds
        self.hand = 0
        self.bust = False
        self.blackjack = False

    def drawCard(self,card):

        if card.getValue() == 1 and (self.hand + 11) <= 21:
            self.hand += 11
        elif card.getValue() == 1 and (self.hand + 11) > 21:
            self.hand += 1
        else:
            self.hand += card.getValue()

        return card

    def getName(self):
        return self.name

    def getFunds(self):
        return self.funds

    def placeBet(self, bet):
        self.hand -= bet
        return bet

    def resetHand(self):
        self.hand = 0
        self.bust = False
        self.blackjack = False

    def getHand(self):
        return self.hand

    def setBust(self):
        self.bust = True

    def getBust(self):
        return self.bust

    def setBlackjack(self):
        self.blackjack = True

    def getBlackjack(self):
        return self.blackjack

class Dealer(Hand):

    def __init__(self):
        super().__init__("House", 500000000)
