# Ben Michener
# 1/29/17
# Intro to Python
# SongCreator

import Epic

# Prompt user for parts of the song
vOne = Epic.userString("Enter the first verse:").upper()
vTwo = Epic.userString("Enter the second verse:").upper()
vThree = Epic.userString("Enter the third verse:").upper()
vFour = Epic.userString("Enter the fourth verse:").upper()
chorus = Epic.userString("Enter the chorus:").lower()
chorusRepeat = Epic.userInt("Enter the chorus repeat:")

# Create full chorus
fullChorus = (chorus + " " ) * chorusRepeat

# Create full song in list form
fullSong = []
fullSong = fullSong + [vOne] + [fullChorus] + [vTwo] + [fullChorus] + [vThree] + [fullChorus] + [vFour] + [(fullChorus + chorus)]

# Replace "COOKIES" with "_______"
i = 0
for line in fullSong:
    fullSong[i] = fullSong[i].replace("COOKIES","_______")
    fullSong[i] = fullSong[i].replace("cookies","_______")
    i = i + 1


print fullSong

# Print list individually
Epic.printList(fullSong)
print "...One more time!..."
Epic.printList(fullSong)