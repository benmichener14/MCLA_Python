#************************************************
#   Ben Michener
#   2/16/2017
#   Intro to Python
#   Exam 2 (RubiksCube.py)
#************************************************
import Epic

#************************************************
# Reads the specified file (filename) and returns a dictionary 
# whose keys are names and whose values are the times
# taken to solve a rubiks cube
#************************************************
def readFile(fileName):
    d = {}
    for line in open(fileName):
        temp = line.split(",")
        name = temp[0]
        d[name] = float(temp[1].strip())
    return d

#************************************************
# Takes a dictionary (d) and separates its keys into separate 
# lists based on the size of the values they hold
#************************************************
def sortTimes(d):
    places = {"Cube Head": [], "Square Master": [], "Advanced Twister": [], "Intermediate Turner": [], "Average Mover": [], "Pathetic" : []}
    for name in d:
        if d[name] < 10:
            places["Cube Head"].append(name)
        elif d[name] < 20:
            places["Square Master"].append(name)
        elif d[name] < 30:
            places["Advanced Twister"].append(name)
        elif d[name] < 40:
            places["Intermediate Turner"].append(name)
        elif d[name] < 60:
            places ["Average Mover"].append(name)
        else:
           places["Pathetic"].append(name)
    return places

#************************************************
# Takes a dictionary (d) and prints each of the values held in the
# list under each key
#************************************************
def printValues(d):
    print "Cube Head (0-9.99):"
    for name in d["Cube Head"]:
        print "\t %s" % name
    print "Square Master (10-19.99):"
    for name in d["Square Master"]:
        print "\t %s" % name
    print "Advanced Twister (20-29.99):"
    for name in d["Advanced Twister"]:
        print "\t %s" % name
    print "Intermediate Turner (30-39.99):"
    for name in d["Intermediate Turner"]:
        print "\t %s" % name
    print "Average Mover (40-59.99):"
    for name in d["Average Mover"]:
        print "\t %s" % name
    print "Pathetic (60 and beyond):"
    for name in d["Pathetic"]:
        print "\t %s" % name
    
#************************************************
# Runs appropriate parts of code
#************************************************
def main():
    d = readFile("RubiksTimes.txt")
    places = sortTimes(d)
    printValues(places)
    

main()