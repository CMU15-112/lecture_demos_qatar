import math

#################################################
# Functions (for you to write)
#################################################


# Check if the triangle defined by points (x1,y1) (x2,y2) (x3,y3) is a right triangle
# Hint: you might need the distance function
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
    print("done")
def testGetHundredsDigit():
    print("done")

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
