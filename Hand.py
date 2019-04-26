import random

class Hand():

    def __init__(self):
        self.hand = 0
        self.bust = False
        self.blackjack = False

    def dealCard(self):
        card = random.randint(1,10)

        if card == 1 and (self.hand + 11) <= 21:
            self.hand += 11
        elif card == 1 and (self.hand + 11) > 21:
            self.hand += 1
        else:
            self.hand += card

        return card

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
