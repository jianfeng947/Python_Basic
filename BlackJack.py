# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 08:41:57 2017

@author: U525369
"""

# 1. Create a function to get a shuffled deck

from random import shuffle

def deck():
    deck = []
    ranks = ['A', '2','3','4','5','6','7','8','9','T','J','Q','K']
    suits = ['H','D','S','C']
    
    for rank in ranks:
        for suit in suits:
            deck.append(suit+rank)
    shuffle(deck)
    return deck

# deck()
print (deck())

# 2. Create a function to count points

def points(hand):
    pointTotal = 0
    for i in hand:
        if (i[1] =='J' or i[1]== 'Q' or i[1]=='K' or i[1]=='T'):
            pointTotal +=10
        elif(i[1] == 'A'):
            if (pointTotal >= 11):
                pointTotal += 1
            else:
                pointTotal += 11
        else:
            pointTotal += int(i[1])
    return pointTotal
points(['D8', 'CA'])

# 3. Create a function to give two cards to dealer and player randomly
# Return a list with both hands
def createHands(oneDeck):
    dealerHand = []
    playerHand = []
    dealerHand.append(oneDeck.pop())
    dealerHand.append(oneDeck.pop())
    playerHand.append(oneDeck.pop())
    playerHand.append(oneDeck.pop())
    
    while (points(dealerHand) <= 16):
        dealerHand.append(oneDeck.pop())
        
    return [dealerHand, playerHand]

# Game loop
game = ""
myDeck = deck()
hands = createHands(myDeck)
dealer = hands[0]
player = hands[1]

while (game != "exit"):
    dealerPoints = points(dealer)
    playerPoints = points(player)
    
    print ("Dealer has:") 
    print (dealer[0])
    
    print ("Player has:") 
    print (player)
    
    if (playerPoints == 21):
        print("Player wins with a BalckJack!")
        break
    elif(playerPoints > 21):
        print("Player Busts with ", str(playerPoints)," points. Dealer Wins")
        break
    elif(dealerPoints > 21):
        print("Dealer Busts with ", str(dealerPoints)," points. Player Wins")
        break
    
    game = input("What is you next action: H: Hit or S: Stand? \n")
    
    if (game == 'H'):
        player.append(myDeck.pop())
    elif (playerPoints > dealerPoints):
        print ("Player wins with", str(playerPoints),"points")
        print ("Dealer has", str(dealer)," with ",str(dealerPoints),"points")
        break
    else:
        print ("Dealer wins")
        print ("Dealer has", str(dealer)," with ",str(dealerPoints),"points")
        break 
    
    
