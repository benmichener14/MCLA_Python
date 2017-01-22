# Ben Michener
# 1/22/2017
# Intro to Python
# Recipe Converter (assignment 1)

print "--- Original Recipe ---"

print "Enter the amount of Flour (cups)",
flour = float(raw_input())
print "Enter the amount of Water (cups)",
water = float(raw_input())
print "Enter the amount of Salt (teaspoons)",
salt = float(raw_input())
print "Enter the amount of Yeast (teaspoons)",
yeast = float(raw_input())
print "Enter the loaf adjustment size (e.g. 2.0 double the size)",
adjustment = float(raw_input())

flour *= adjustment
water *= adjustment
salt *= adjustment
yeast *= adjustment

print ""
print "--- Modified Recipe ---" 
print "Flour %.2f cups" %flour
print "Water %.2f cups" %water
print "Salt %.2f teaspoons" %salt
print "Yeast %.2f teaspoons" %yeast
print "Happy Baking!"

#Conversion Factors
flourGram = 120
waterGram = 237
saltGram = 5
yeastGram = 3

print ""
print "--- Modified Recipe in Grams ---"
print "Flour %.2f grams" %(flour * flourGram)
print "Water %.2f grams" %(water * waterGram)
print "Salt %.2f grams" %(salt * saltGram)
print "Yeast %.2f grams" %(yeast * yeastGram)
print "Happy Baking!"