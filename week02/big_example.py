import math

#################################################
# Functions (for you to write)
#################################################

# Calculate the distance between (x1,y1) and (x2,y2)
def distance(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2)**0.5
    return d

# Check if two circles intersect, return True or False
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1,y1,x2,y2)
    if d > r1+r2:
        return False
    else:
        return True

# Get the ones digit from a number.  That number could be an int or a float.
def getOnesDigit(n):
    n = abs(n)
    return int(n)%10

# Get the hundreds digit from a number.  That number could be an int or a float.
def getHundredsDigit(n):
    n = abs(n)
    n = int(n)
    n = n // 100
    return getOnesDigit(n)

#################################################
# Test Functions
#################################################

def testDistance():
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
    
def testGetHundredsDigit():
    print("Testing getHundredsDigit...", end="")
    assert( getHundredsDigit(123) == 1 )
    assert( getHundredsDigit(4237) == 2 )
    assert( getHundredsDigit(23) == 0 )
    assert( getHundredsDigit(-324732) == 7 )
    assert( getHundredsDigit(91223.87) == 2 )
    assert( getHundredsDigit(0) == 0 )
    assert( getHundredsDigit(-91223.87) == 2 )
    assert( getHundredsDigit(345+1200) == 5 )
    print("done.")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testDistance()
    testCirclesIntersect()
    testGetOnesDigit()
    testGetHundredsDigit()

def main():
    testAll()

if __name__ == '__main__':
    main()
    