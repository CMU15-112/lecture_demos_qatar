import math

#################################################
# Functions (for you to write)
#################################################

# Determine if a number is a "fair" number
# We will say that a value n is "fair" if it is an integer and
# it has the same number of even digits as odd digits (ignoring
# leading 0's). A "small fair" number is a fair number with exactly
# 4 digits.
#
# For example, 1083, 1081, and -1092 are each small fair numbers
# because each have two odds and two evens.
#
# With this in mind, and without using strings or loops, write the
# function isSmallFair(n) that takes a value n, that may or may not
# be an integer, and returns True if n is a small fair number, and
# False otherwise. Do not crash if n is not an integer!
def isSmallFair(n):
    return False

# Determine if a triangle is a right triangle given its coordinates
def isRightTriangle(x1, y1, x2, y2, x3, y3):
    return False

# Write the function hourDifference(currentHour, interval) that takes
# as input the current hour as an integer and a number of hours and
# returns where the hour hand will point after interval hours.
# For example...
# - hourDifference(1,3) == 4  (because 1:00 + 3 hours is 4:00)
# - hourDifference(10,4) == 2 (because 10:00 + 4 hours is 2:00)
def hourDifference(currentHour, interval):
    return 42

#################################################
# Test Functions
#################################################

def testIsSmallFair():
    print("Testing isSmallFair...", end="")
    assert(isSmallFair(1234))
    assert(isSmallFair(-1234))
    assert(isSmallFair(15112) == False)
    assert(isSmallFair("1234") == False)
    assert(isSmallFair(1234.0) == False)
    assert(isSmallFair(-1234))
    assert(isSmallFair(1123)==False)
    assert(isSmallFair(2234)==False)

def testIsRightTriangle():
    print("Testing isRightTriangle ...")
    assert(isRightTriangle(0, 0, 3, 0, 0, 4) )
    assert(isRightTriangle(3, 0, 0, 0, 0, 4) )
    assert(isRightTriangle(0, 4, 3, 0, 0, 0) )
    assert(isRightTriangle(0, 0, 1, 1, 100, 0) == False)
    assert(isRightTriangle(0,0,5,0,0,10))
    print("passed!")
    
def testHourDifference():
    print("We need to write some testcases here!")
    print("Be sure to write them *before* writing the solution.")
    print("Try some strange things, like interval being more than 24 hours.")


#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testIsSmallFair()
    testIsRightTriangle()
    testHourDifference()

def main():
    testAll()

if __name__ == '__main__':
    main()
