#Gets Int from user
def userInt(prompt):
    print prompt,
    num = int(raw_input())
    return num

# Gets string from user
def userString(prompt):
    print prompt,
    s = raw_input()
    return s

#Prints list individually    
def printList(list):
    i = 0
    for line in list:
        print list[i]
        i = i + 1