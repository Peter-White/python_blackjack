from Hand import *

def score(player, dealer):
    print("\n")
    print("===========================")
    print(f"Player: {player.getHand()}")
    print(f"Dealer: {dealer.getHand()}")
    print("===========================")
    print("\n")

player = Hand()
dealer = Hand()

player.dealCard()
player.dealCard()
dealer.dealCard()

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
        print(f"\nYou draw a {player.dealCard()}")
    elif move == "stand":
        print("\nPlayer Stand's")
        break
    else:
        print("\nInvalid")

print("\nDealer flips a {}".format(dealer.dealCard()))

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
            print("\nDealer draws a {}".format(dealer.dealCard()))
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