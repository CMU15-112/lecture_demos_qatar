import math

#################################################
# Functions (for you to write)
#################################################

# Calculate the distance between (x1,y1) and (x2,y2)
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.6

# Check if two circles intersect, return True or False
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    return False

# Get the ones digit from a number.  That number could be an int or a float.
def getOnesDigit(n):
    return 42

# Get the hundreds digit from a number.  That number could be an int or a float.
def getHundredsDigit(n):
    return 42

#################################################
# Test Functions
#################################################

def testDistanceBad():
    print("Testing distance...", end="")
    val = distance(0,0,3,4)
    if val != 5:
        print("Distance is broken! I got", val)
        
    val = distance(7,4,25,7)
    if math.isclose(val, 333 ** 0.5) == False:
        print("Distance is broken! I got", val)
    print("done.")
    
def testDistance():
    print("Testing distance...", end="")
    assert distance(0,0,3,4) == 5
    assert math.isclose(distance(7,4,25,7), 333 ** 0.5)
    print("done.")


#################################################
# testAll and main
#################################################

def testAll():
    testDistance()

def main():
    testAll()

if __name__ == '__main__':
    main()