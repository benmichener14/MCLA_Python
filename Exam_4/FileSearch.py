#************************************************
#   Ben Michener
#   2/16/2017
#   Intro to Python
#   Exam 4 (FileSearch.py)
#************************************************
import Epic
import os

#************************************************
#   Searches the folder for .txt files and includes
#   them as a key in a dictionary, with their assigned
#   lists being the lines in the file themselves
#************************************************
def readFiles():
    files = os.listdir(".")
    fileList = {}
    for name in files:
        if ".txt" in name:
            fileList[name] = []
            for line in open(name):
                temp = line.split("\n")
                fileList[name].append(temp[0].strip().upper())
    return fileList
            
#************************************************
#   Searches the dictionary key by key and line by 
#   line within said keys for a search term. When one
#   is found, a counter is incrumented, and the name of
#   the file is printed, along with the line it was found
#   on.
#************************************************
def fileContains(fileList, word):
    counter = 0
    for fileName in fileList.keys():
        for line in fileList[fileName]:
            if word in line:
                print "%s: %s" % (fileName, line)
                counter = counter + 1
    return counter

#************************************************
#   Prompts a user for a string they wish to search 
#   for and searches all of the .txt files in the same
#   directory as this program for said string. Displays
#   all instances of the string in the files, along with
#   what files they were found in, and a final count of
#   how many times it occurred across all of the files
#************************************************
def main():
    word = Epic.userString("What word do you want to search for?").upper()
    
#    included = Epic.userString("Do you want to include words that include the search term inside them? (y or n)")
#    if included == "n":
#        word = " " + word + " "
# Not included because I was running into some bugs with it. Basically, if I searched for very common words (Such as "a"), the program would not
# run all the way through to display all occurences of it as an isolated word, and it would stop at a seemingly random point in the search without
# displaying the number of times it occured (which would have signified that the search completed). I believe this is something to do with a limit
# to the number of lines that can be displayed in the terminal. If this were not a timed exam, I would play with it for another hour or so. 
# mind if I stop by your office hours this wednesday to talk about this?
        
    fileList = readFiles()
    
    count = fileContains(fileList, word)
    print ("Here is all %s cases of \"%s\" I found in the files.") % (count, word)
    
    
main()