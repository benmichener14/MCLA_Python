#************************************************
#   Ben Michener
#   3/26/2017
#   Intro to Python
#   PerfectShuffle.py
#************************************************

import Epic
import random

rank = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suit = ["Clubs", "Hearts", "Diamonds", "Spades"]

#************************************************
#   Creates the deck that will be used throughout
#   the program by appending each combination of 
#   suit and card to the "deck" list
#************************************************

def buildDeck(rank, suit):
    deck = []
    for n in rank:
        for i in suit:
            deck.append(n + " of " + i)
    return deck
    
#************************************************
#   Does the "Perfect Shuffle" once by splitting 
#   the deck and then appending corresponding 
#   values to a new list in ascending order.
#   NOTE:
#   You recommended using the modulo opperator 
#   here, yet I found that completely unnecessary
#   and overly complicated when there is an easier
#   way to accomplish the same goal with one loop.
#************************************************

def perfectShuffle(deck):
    deckOne = deck[0 : 26]
    deckTwo = deck[26 : 52]
    newDeck = []
    for i in range(0 , 26):
        newDeck.append(deckOne[i])
        newDeck.append(deckTwo[i])
    return newDeck
    
#************************************************
#   Shuffles the deck randomly, as per the "Level
#   Up" requirements. I could have programmed my 
#   own unique way to randomize this, but why bother
#   when there is already a module that does exactly
#   that? Also, instead of creating a whole new
#   program to simply do this form of shuffle, I
#   added a choice in main(). It seeed like a more
#   efficient way of doing things.
#************************************************
    
def randomShuffle(deck):
    random.shuffle(deck)
    return deck

#************************************************
#   Returns a five card hand from a given deck.
#************************************************
    
def deal(deck):
    hand = deck[0 : 5]
    return hand

#************************************************
#   Creates and shuffles a standard 52 card deck
#   per the requests of a user. The program prompts
#   the user about whether they want a random shuffle
#   or a perfect shuffle, and how many times they
#   wish to do each shuffle. The program then returns
#   a five card hand from the shuffled deck.
#************************************************

def main():
    deck = buildDeck(rank, suit)
    shuffle = Epic.userString("Do you want to do a \"random\" shuffle or a \"perfect\" shuffle?")
    times = Epic.userInt("How many times do you want to shuffle the deck?")
    if shuffle.lower() == "random":
        for i in range(0, times):
            deck = randomShuffle(deck)
    elif shuffle.lower() == "perfect":
        for i in range(0, times):
            deck = perfectShuffle(deck)
    else:
        print "You did not choose an appropriate type of shuffle. This program will now end."
        quit()
    
    hand = deal(deck)
    print hand

main()