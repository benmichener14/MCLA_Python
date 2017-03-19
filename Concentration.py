import Epic
import random
import time

def randomize(cardList):
    index = random.randrange(0, 8)
    cardList.append(cardList[index])
    random.shuffle(cardList)
    return cardList
    
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