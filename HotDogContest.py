#************************************************
#   Ben Michener
#   2/16/2017
#   Intro to Python
#   HotDogContest.py
#************************************************

import Epic
import random
import time

#************************************************
# Prompts the user for a contestant and an amount to bet
# and returns that information
#************************************************
def userBet(cash):
    guess = Epic.userString("Who do you wish to bet on? (Tim, James, Katherine)")
    money = Epic.userInt("How much do you wish to bet? (cash = %s)" % cash)             #The user can bet more money than they have. I like keeping this in because
    bet = {"guess": guess, "money": money}                                              #it makes the program a bit more fun. bet 60 when I only have 50? Sure, if it
    return bet                                                                          #is worth the risk....
    
#************************************************
# Runs the hot dog contest, adding a random number of
# hot dogs to each contestant. This continues until someone 
# gets over 50 hot dogs. Returns the winner
#************************************************
def contestRun(contestants):
    while contestants["Tim"] <= 50 and contestants["James"] <= 50 and contestants["Katherine"] <= 50:
        time.sleep(1)
        print "\n much... munch... munch... \n"
        time.sleep(1)
        contestants["Tim"] = contestants["Tim"] + random.randrange(1,5)                 #No parameters for number of hot dogs per turn were given. Numbers chosen arbitrarily
        contestants["James"] = contestants["James"] + random.randrange(1,5)
        contestants["Katherine"] = contestants["Katherine"] + random.randrange(1,5)
        
        print "Tim has eaten %s hot dogs!" % contestants["Tim"]
        print "James has eaten %s hot dogs!" % contestants["James"]
        print "Katherine has eaten %s hot dogs!" % contestants["Katherine"]
        
    if contestants["Tim"] > 50:
        winner = "Tim"
    elif contestants["James"] > 50:
        winner = "James"
    elif contestants ["Katherine"] > 50:
        winner = "Katherine"
    
    return winner
    
#************************************************
# This program allows the user to bet some money on 
# three contestants in a hot dog eating contest.
# The contest then runs and the contestant who eats 
# over 50 hot dogs first wins. If the user bet correctly,
# they win back the money they bet, and if they lose, they
# lose that money. They can continue until they lose all their
# money.
#************************************************
def main():
    cash = 100
    while cash > 0:
        contestants = {"Tim" : 0, "James": 0, "Katherine": 0}
        bet = userBet(cash)
        print "Let's start the contest!"
        winner = contestRun(contestants)
        if winner == bet["guess"]:
            print "\nYou guessed it right! %s won!" % winner
            print "you won %s dollars" % bet["money"]
            cash = cash + bet["money"]
        elif winner != bet["guess"]:
            print "\nYou guessed it wrong! %s won instead!" % winner
            print "you lost %s dollars" % bet["money"]
            cash = cash - bet["money"]
        print "You have %s dollars" % cash
        
        
        
    
main()