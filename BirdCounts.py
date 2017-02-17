#----------------------------------------
#   Ben Michener
#   2/17/17
#   Intro to Python
#   Assignment 4 - BirdCounts.py
#----------------------------------------

import Epic

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen. 
# ------------------------------------------------------------
def countBirds(filename):
    d = {}
    for line in open(filename):
        temp = line.split(",")
        bird = temp[0].strip().lower()
        spottings = int(temp[1].strip())
        if bird in d:                           #If the bird is already in dictionary(d), add the spottings to already present value
            d[bird] = d[bird] + spottings
        else:                                   #If not, add the bird and the spottings to dictionary(d)
            d[bird] = spottings
    return d
    
# ------------------------------------------------------------
# Determines and prints the highest spotted bird(s) 
# in a dictionary(d)
# ------------------------------------------------------------
def highestSpottings (d):
    highest = 0
    highestBirds = []
    for bird in d:                              #Find highest value of spotted birds
        if d[bird] > highest:
            highest = d[bird]
    for bird in d:                              #Add all birds with said value of spots to a list of the highest spotted birds
        if d[bird] == highest:
            highestBirds.append(bird)
    print "Your highest spoted bird(s) is",
    for i in range(0, len(highestBirds)):       #Print the list of hightest spotted birds (one bird at a time)
        print "the %s" %highestBirds[i] ,
        if i != (len(highestBirds) - 1):
            print "and",
    print ""
    
# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d). 
# ------------------------------------------------------------
def askUser(d):
    bird = Epic.userString("What bird do you want to look up? (enter \"exit\" to end the program)").lower()
    cont = True
    if bird == "exit":
        cont = False
    elif bird in d:
        print "I have seen that bird %s time(s)" % d[bird]
        highestSpottings(d)
    else:
        print "I have seen that bird 0 time(s)"
        highestSpottings(d)
    
    return cont
    
# ------------------------------------------------------------
# Runs and loops appropriate parts of code
# ------------------------------------------------------------
def main():
    d = countBirds("Birds.txt")
    cont = True
    while cont == True:
        cont = askUser(d)
    
    
    
main()