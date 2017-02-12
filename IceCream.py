import Epic

def getFlavors():
    i = 0
    flavors = []
    while i < 5:
        iceCream = Epic.userString("Please enter an ice cream flavor.").lower()
        flavors.append(iceCream)
        i = i + 1
    return flavors
    
def countInStock(flavors):
    inStock = ["vanilla", "chocolate", "strawberry"]
    c = 0
    for iceCream in flavors:
        if iceCream in inStock:
            c = c + 1
    return c
            
    
def main():
    flavs = getFlavors()
    print flavs
    c = countInStock(flavs)
    print "We have %s of your flavors" % c
    
main()