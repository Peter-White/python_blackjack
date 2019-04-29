from Hand import *
from Card import *
from Deck import *

playingDeck = Deck()

def score(player, dealer):
    print("\n")
    print("===========================")
    print(f"Player: {player.getHand()}")
    print(f"Dealer: {dealer.getHand()}")
    print("")
    print(f"{playingDeck.remainingCards()} cards in Deck")
    print("===========================")
    print("\n")

player = Hand("The Cincinnati Kid", 500)
dealer = Dealer()
playingDeck.shuffleCards()

pool = 0

def playerPlaceBet(Player,minBet=10):
    bet = 0

    if Player.getFunds() < minBet:
        print("Your funds do not match the minimum bet you cannot play")
        bet = -1
    else:
        while bet < minBet:
            ans = input(f"The minimum is ${minBet} enter match or raise: ").lower()

            if ans == "raise":
                place_bet = int(input("Enter the amount to raise by: "))

                if place_bet <= 0:
                    print("You cannot bet less than zero funds")
                elif place_bet + minBet > Player.getFunds():
                    print("You cannot bet more than your current funds")
                else:
                    print(f"You bet ${Player.placeBet(place_bet)}", end='')
                    print(f" and raised the minimum to ${minBet + place_bet}")
                    bet = minBet + bet
            elif ans == "match":
                print("You match the minimum with ${}".format(Player.placeBet(minBet)))
                bet = minBet
            else:
                print("Invalid. Try Again.")

    return bet

def playGame():

    if playingDeck.remainingCards() < 20:
        print("Reshuffling Decks")
        playingDeck.shuffleCards()

    print("\n")
    print("Player starts with a {} and a {}".format(player.drawCard(playingDeck.dealCard()).getTitle(),player.drawCard(playingDeck.dealCard()).getTitle()))
    print("Dealer starts with a {}".format(dealer.drawCard(playingDeck.dealCard()).getTitle()))
    print("\n")

    while True:

        if player.getHand() > 21:
            print("Player's hold is {}".format(player.getHand()))
            print("Player Busts")
            player.setBust()
            break
        if player.getHand() == 21:
            print("Player's hold is {}".format(player.getHand()))
            print("Player Blackjack's")
            player.setBlackjack()
            break

        score(player, dealer)

        move = input("Do you want to hit or stand? ").lower()

        if move == "hit":
            print(f"\nYou draw a {player.drawCard(playingDeck.dealCard()).getTitle()}")
        elif move == "stand":
            print("\nPlayer Stand's")
            break
        else:
            print("\nInvalid")

    print("\nDealer flips a {}".format(dealer.drawCard(playingDeck.dealCard()).getTitle()))

    while True:
        score(player, dealer)

        if not player.getBust():
            if dealer.getHand() > 21:
                print("Dealer busts")
                dealer.setBust()
                break
            elif dealer.getHand() == 21:
                print("Dealer Blackjack's")
                dealer.setBlackjack()
                break
            elif dealer.getHand() >= 17:
                print("Dealer stands")
                break
            else:
                print("\nDealer draws a {}".format(dealer.drawCard(playingDeck.dealCard()).getTitle()))
        else:
            break

    if player.getHand() == dealer.getHand():
        print("\nPush")
    elif player.getBust() == True:
        print("\nDealer Wins By Default")
    elif dealer.getBust() == True:
        print("\nPlayer Wins By Default")
    elif player.getBlackjack() == True:
        print("\nPlayer Wins By Blackjack")
    elif player.getHand() > dealer.getHand():
        print("\nPlayer Wins")
    elif dealer.getBlackjack() == True:
        print("\nDealer Wins By Blackjack")
    else:
        print("\nDealer Wins")

game_over = False
while not game_over:
    playGame()

    while True:
        ans = input("\nPlay another hand (y/n)? ").lower()

        if ans == "n":
            print("Come back soon with more money")
            game_over = True
            break
        elif ans == "y":
            print("Dealing again")
            player.resetHand()
            dealer.resetHand()
            break
        else:
            print("Invalid")
