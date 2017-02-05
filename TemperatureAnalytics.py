# Ben Michener
# 2/4/17
# Intro to Python
# TemperatureAnalytics (assignment 3)

import Epic

# Read temps from the file
# and return them in a list
def readTemps():
    values = []
    file = open("temps.txt")
    for line in file:
        value = line.split("\n")
        temp = value[0]
        values.append(float(temp))
    return values
    

# Calculates the average range of numbers
# as defined by start(inclusive) and stop(inclusive)
def calculateAvg(values, start, stop):
    i = start
    total = 0.0
    while( i < stop):                       #i being the position of the value being analyzed in the list
        total = total + values[i]           #adding each value to total
        i = i + 1                           #Incrument i
    total = total / (stop - start)          #Finding mean using the total previously calculated and the number of values analyzed
    return total
    

# Counts all values that have a positive deviation
# in the range specified as start(inclusive)
# and stop (inclusive)
def count(values, start, stop):
    i = start
    positive = 0
    while( i < stop):                       # i being the position of the value being analyzed in the list
        if (values[i] > 0):
            positive = positive + 1         #Incrument number of positive values in set
        i = i + 1                           #Incrument i
    return positive
    
    

# main function
# data downloaded from http://climate.nasa.gov/
# data represents the deviation in global surface
# temperature relative to 1951-1980 average temperatures.
def main():
    values = readTemps()
    
    percent = Epic.userString("What percentage of the values do you want to analyze (decimal)")
    stop = round((len(values) * float(percent)), 0)     #stop being the uppermost number in this set
    start = 0                                           #start being the lowermost number in this set
    
    total = calculateAvg(values, start, stop)
    print "During the first %s years, the average deviation from the temperature anomoly is %s" % (stop, total)
    
    positive = count(values, start, stop)
    print "During the first %s years, %s had a positive temperature anomaly." % (stop, positive)
    
    start = int(stop)           # Adjust start and stop values for second half of data being analyzed
    stop = int(len(values)) 
    
    total = calculateAvg(values, start, stop)
    print "During the next %s years, the average deviation from the temperature anomoly is %s" % ((stop - start), total)
    
    positive = count(values, start, stop)
    print "During the next %s years, %s had a positive temperature anomaly." % ((stop - start), positive)
    

main()