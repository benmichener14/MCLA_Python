#************************************************
#   Ben Michener
#   4/30/2017
#   Intro to Python
#   Exam 6 (Clue.py)
#************************************************
import Epic

#************************************************
#   Removes a selected term from the appropriate 
#   list. Returns altered list.
#************************************************
def removeTerm(clue, possible):
    term =  Epic.userString("Enter the %s that was not involved with the murder: (%s)" % (clue, possible)).lower()
    if term in possible:
        possible.remove(term)
    return possible

#************************************************
#   Loops through each list and provides the number
#   of different combinations. When there is only
#   one combination, then it displays what it is.
#************************************************
def search(people, weapons, rooms):
    i = 0
    for p in people:
        for w in weapons:
            for r in rooms:
                i = i + 1

    if i == 1:
        print "There's only one possibility! It was %s in the %s with a %s!" %(p, r, w)
        return i
    else:
        return i
    
#************************************************
#   Assists the user in discovering who commited
#   murder. All people, weapons, and rooms from the
#   original game of clue are included. 
#************************************************
def  main():
    people = ["miss scarlett", "colonel mustard", "mrs. white", "mr. green", "mrs. peacock", "professor plum"]
    weapons = ["candlestick", "knife", "lead pipe", "revolver", "rope", "wrench"]
    rooms = ["conservatory", "lounge", "kitchen", "library", "hall", "study", "ballroom", "dining room", "billiard room"]
    i = 0
    
    while i != 1:
        clue = Epic.userString("Is the clue about a person (p), a weapon (w), or a room (r)").lower()
            
        if clue == "p":
            people = removeTerm("person", people)
        elif clue == "w":
            weapons = removeTerm("weapon", weapons)
        elif clue == "r":
            rooms = removeTerm("room", rooms)
                
        i = search(people, weapons, rooms)
        
        if i != 1:
            print "There are %s possibilities left." % i
    
    
main()