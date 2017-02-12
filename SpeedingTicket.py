#*************************
#   Ben Michener
#   2/12/17
#   Intro to Python
#   Exam #1 - SpeedingTicket
#*************************

import Epic

#*************************
# Reads speed of specified file
# and returns in list form
#*************************
def readData(filename):
    values = Epic.fileToList(filename)
    return values

#*************************
# finds & returns the average 
# speeds of a given list
#*************************
def getAverage(values):
    total = 0
    for speed in values:
        total = total + float(speed)
    mean = total / len(values)
    return mean
    
#*************************
# Counts & returns the number of values
# over a given constant
#*************************    
def countSpeeders(values, maxSpeed):
    i = 0
    for speed in values:
        if (float(speed) > float(maxSpeed)):
            i = i + 1
    return i

#*************************
# Finds the average speeds of people during rush
# hour and not rush hour on a given day, counts the 
# number of people speeding, and calculates the total
# speeding fines
#*************************    
def main():
    maxSpeed = Epic.userInt("What is the speed limit in the area?")
    
    # Get data from files and return the in list form
    rush = readData("data-rush.txt")
    notRush = readData("data-not-rush.txt")
    
    # Finds average of the lists
    rushAverage = getAverage(rush)
    notRushAverage = getAverage(notRush)
    
    print "The average speed during rush hour was %.2f" % rushAverage
    print "The average speed not during rush hour was %.2f" % notRushAverage
    
    # Finds total people speeding and calculates fines
    totalRush = countSpeeders(rush, maxSpeed)
    rushFine = int(totalRush) * 150
    totalNotRush = countSpeeders(notRush, maxSpeed)
    notRushFine = int(totalNotRush) * 100
    
    print "There were %s speeders during rush hour. Total fine = $ %s" % (totalRush, rushFine)
    print "There were %s speeders not during rush hour. Total fine = $ %s" % (totalNotRush, notRushFine)
    
main()