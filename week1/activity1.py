import math

#################################################
# Functions (for you to write)
#################################################


# Check if the triangle defined by points (x1,y1) (x2,y2) (x3,y3) is a right triangle
# Hint: you might to write the distance function
def isRightTriangle(x1, y1, x2, y2, x3, y3):
    return False

# Get the hundreds digit from a number.  That number could be an int or a float.
# Hint: use integer division // and mod %
def getHundredsDigit(n):
    return 42

#################################################
# Test Functions
#################################################
def testIsRightTriangle():
    print("Testing isRightTriangle ...", end="")
    assert(isRightTriangle(0, 0, 3, 0, 0, 4) )
    print("passed!")
    
def testGetHundredsDigit():
    print("Testing getHundredsDigit ...", end="")
    assert(getHundredsDigit(321) == 3)
    print("passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testIsRightTriangle()
    testGetHundredsDigit()

def main():
    testAll()

if __name__ == '__main__':
    main()