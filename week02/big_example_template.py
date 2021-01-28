import math

#################################################
# Functions (for you to write)
#################################################

# Calculate the distance between (x1,y1) and (x2,y2)
def distance(x1, y1, x2, y2):
    return 42 

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

def testDistance():
    print("Testing distance...", end="")
    val = distance(0,0,3,4)
    if val != 5:
        print("Distance is broken")
        
    val = distance(7,4,25,7)
    if val != 333**0.5:
        print("Distance is broken")
    print("done.")

def testDistanceBetter():
    print("Testing distance...", end="")
    assert( math.isclose(distance(0,0,3,4),5) )
    assert( math.isclose(distance(7,4,25,7),333**0.5) )
    print("done.")

def testCirclesIntersect():
    print("Testing circlesIntersect...", end="")
    assert( circlesIntersect(0,0,1,5,5,3) == False )
    assert( circlesIntersect(0,0,3,2,2,4) == True )
    assert( circlesIntersect(0,0,5,0,0,5) == True )
    assert( circlesIntersect(0,0,3,6,0,3) == True )
    assert( circlesIntersect(0,0,2,0,0,4) == True )
    print("done.")

def testGetOnesDigit():
    print("Testing getOnesDigit...", end="")
    assert( getOnesDigit(123) == 3)
    assert( getOnesDigit(4237) == 7)
    assert( getOnesDigit(0) == 0)
    assert( getOnesDigit(2) == 2)
    assert( getOnesDigit(2.3) == 2)
    assert( getOnesDigit(-123) == 3)
    print("done.")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testDistance()
    testCirclesIntersect()
    testGetOnesDigit()

def main():
    testAll()

if __name__ == '__main__':
    main()
    