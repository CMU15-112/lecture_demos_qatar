import math

#################################################
# Functions (for you to write)
#################################################


# Check if the triangle defined by points (x1,y1) (x2,y2) (x3,y3)
# is a right triangle
# Hint: you may need the distance function
def isRightTriangle(x1, y1, x2, y2, x3, y3):
    return False

# We will say that a value n is a "small 42ish" if it is an integer number
# with precisely four digits and has two consecutive numbers that form
# the number 42.
# For example, 4212, 5042, and -6422 are small 42ish numbers because
# they have four digits, and the number 42 appears inside these numbers.
#With this in mind, and without using strings or loops,
# write the function isSmall42ish(n) that takes a value n,
# which may or may not be an integer, and returns True
# if n is a small 42ish number, and False otherwise.
# Do not crash if n is not an integer! Do not use strings or loops here.

def isSmall42ish(n):
    return False

# Use nested for-loops to print a diamond shape made of
# the character '*' where the number of rows is equal
# to the input argument "nrows". Assume nrows is even.
# The top half of the diamond should be a triangle made of '*'
# and the bottom half should be the mirror image of the
# top half.
# Examples:
"""
printDiamondStarShape(6)
  *  
 *** 
*****
*****
 *** 
  *  

printDiamondStarShape(10)
    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    *
"""
def printDiamondStarShape(nrows):
    print(42)
    
#################################################
# Test Functions
#################################################
def testIsRightTriangle():
    print("Testing isRightTriangle ...", end="")
    assert(isRightTriangle(0, 0, 3, 0, 0, 4) )
    print("passed!")
    
def testIsSmall42ish():
    print("Testing isSmall42ish ...", end="")
    assert(isSmall42ish(321) == False)
    assert(isSmall42ish(42) == False)
    assert(isSmall42ish(4200) == True)
    assert(isSmall42ish("4200") == False)
    print("passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testIsRightTriangle()
    testGetHundredsDigit()
    print("No testcases for printDiamonStarShape")

def main():
    testAll()

if __name__ == '__main__':
    main()