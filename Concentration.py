#************************************************
#   Ben Michener
#   3/19/2017
#   Intro to Python
#   Exam  (Concentration.py)
#************************************************
import Epic
import random
import time

#************************************************
#   Randomizes the given list and creates the one duplicate card
#   for the game, setting up and returning the playing board
#************************************************

def randomize(cardList):
    index = random.randrange(0, 8)
    cardList.append(cardList[index])
    random.shuffle(cardList)
    return cardList
    
#************************************************
#   Runs the game, asking the user to pick two cards and
#   comparing to see if they are a matching pair. Keeps track
#   of and returns the number of tries it took to get the matching pair.
#   Also checks to see if the numbers are out of bounds and if the
#   user tried to pick two of the same number
#************************************************

def gameRun(randomizedList):
    win = False
    turns = 1
    while win == False:
        gOne = Epic.userInt("Pick the first card to turn over. (0 - 9)")
        gTwo = Epic.userInt("Pick the second card to turn over. (0 - 9)")
        while gOne < 0 or gOne > 9 or gTwo < 0 or gTwo > 9 or gOne == gTwo:
            print "Invalid choices. You must pick different cards and each card must be a number between 0 and 9."
            gOne = Epic.userInt("Pick the first card to turn over. (0 - 9)")
            gTwo = Epic.userInt("Pick the second card to turn over. (0 - 9)")
        
        print "Card %s is a %s" % (gOne, randomizedList[gOne])
        print "Card %s is a %s" % (gTwo, randomizedList[gTwo])
        
        if randomizedList[gOne] == randomizedList[gTwo]:
            print "Nice! You got it!"
            win = True
        else:
            turns = turns + 1
    return turns
    
#************************************************
#   Plays a game of concentration with the user, with
#   one correct matching pair. Gives a rating to the user based
#   on how long it took to find the correct pair.
#************************************************
    
def main():
    cardList = ["bird", "dog", "snake", "fish", "cat", "mouse", "starfish", "woodchuck", "crab"]
    print "Welcome to Concentration!"
    print "Hold on, we are tailoring a list exactly to your needs..."
    
    randomizedList = randomize(cardList)
    
    print("\n...")
    time.sleep(1)
        
    print("\n")
    print "Perfect! We're ready to play! \n"
    
    turns = gameRun(randomizedList)
    
    if turns < 3:
        print "Nice job! You're a master at this game! ",
    elif turns <= 6:
        print "Not bad! You did pretty well! ",
    elif turns <= 9:
        print "Okay! You managed to get it eventually... ",
    elif turns > 9:
        print "I don't think this is your game... ",
    
    print "It took you %s turns to find the matching pair." % turns

main()