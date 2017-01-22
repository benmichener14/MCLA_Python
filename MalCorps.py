# Ben Michener
# 1/21/2017
# MalCorps.py
# Intro to Python - You Try It #1

print "How many MalCorps did you find on planet Exflon?",
numOne = raw_input()
print "How many MalCorps did you find on planet Mobiles?",
numTwo = raw_input()
print "How many MalCorps did you find on planet Monsantoes",
numThree = raw_input()

numTotal = int(numOne) + int(numTwo) + int(numThree)

print "You found %s MalCorps!" %(numTotal)

print "The average MalCorps per planet is %.2f" %(numTotal / 3.0)