#************************************************
#   Ben Michener
#   4/16/2017
#   Intro to Python
#   Exam 5 (PetStore.py)
#************************************************
import json
import Epic

#************************************************
#   Reads in the json file and returns it to main
#************************************************
def readFile(fileName):
    jsonTxt = ""
    f = open(fileName)
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    inventory = json.loads(jsonTxt)
    return inventory
    
#************************************************
#   Searches the json file by either category or
#   keyword, then prints all that conincide with
#   the search term.
#************************************************
def searchFile(inventory, search):
    if search == "c":
        term = Epic.userString("Which category do you wish to search for?").lower()
        for item in inventory:
            if item["Category"].lower() == term:
                print "%s - $%s" % (item["Product"], item["Price"])
    elif search == "k":
        term = Epic.userString("What do you want to search for?").lower()
        for item in inventory:
            if term in item["Product"].lower():
                print "%s - $%s" % (item["Product"], item["Price"])
    else:
        print "You did not enter an appropriate string. This program will now end."
            
            
#************************************************
#   Allows the user to search a json file by 
#   either category or keyword and get a list of
#   all the products in the json file that match
#   up with the search parameters
#************************************************   
def main():
    inventory = readFile('PetStore.json')
    search = Epic.userString("Search by Category (c) or by Keyword (k)").lower()
    searchFile(inventory, search)


main()

#************************************************
#   Sorry for the bland program this week. I'm rushing
#   to finish this before my parents come up to celebrate
#   my birthday a couple days early. If I spent more time
#   on this, I would have added contingencies for cases
#   where they searched for a term that is not present
#   in the json file. I also would have spiced up the 
#   formatting of what is printed to the console and
#   probably just given it my own flair. But it satisfies
#   all of the requirements, so it's good for now.
#
#   I promise I'll make a more interesting program this week!
#
#       -Ben
#************************************************