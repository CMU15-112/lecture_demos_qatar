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
    
    #smallFair: 4 digits, # odd digits equals # even digits
    
    # if n is not integer, return false
    if type(n) != int:
        return False
    
    # absolute value of n has to be between 1000 and 9999, otherwise return False
    n = abs(n)
    if n < 1000 or n > 9999:
        return False
    
    # check that the number of even digits equals the number of odd digits (2 even and 2 odd)
        #get each digit
            #integer division over multiples of 10 and mod 10
    
    d4= n%10
    d3= (n//10)%10
    d2= (n//100)%10
    d1= (n//1000)
    
        #identify odd from even digits
            # sum of mod2 for all the digits
    sumMods= d1%2 + d2%2 + d3%2 + d4%2        
            
    #if sum is equla to 2, retrun True
    
    #false otherwise 
    
    return (sumMods == 2)

def distance(p1x, p1y, p2x, p2y):
    dist= ((p1x-p2x)**2 + (p1y-p2y)**2)**0.5
    return dist
    

# Determine if a triangle is a right triangle given its coordinates
def isRightTriangle(x1, y1, x2, y2, x3, y3):
    
    #calculate the sides lengths given the verticies coordinates
    s1= distance(x1, y1, x2, y2)
    s2= distance(x2, y2, x3, y3)
    s3= distance(x1, y1, x3, y3)
    
    # if the sum of the square of two sides equals the square of the third side return, True
    if math.isclose((s1**2+s2**2),  s3**2):
        return True
    if math.isclose((s2**2 + s3**2), s1**2):
        return True
    
    if math.isclose((s1**2 + s3**2), s2**2):
        return True

    # otherwise False
    
    return False

# Write the function hourDifference(currentHour, interval) that takes
# as input the current hour as an integer and a number of hours and
# returns where the hour hand will point after interval hours.
# For example...
# - hourDifference(1,3) == 4  (because 1:00 + 3 hours is 4:00)
# - hourDifference(10,4) == 14 (because 10:00 + 4 hours is 14:00)
def hourDifference(currentHour, interval):
    
    # check if hour is not int, return -1
    if type(currentHour) != int:
        return -1
    
    # hour is between 0 and 23
    if currentHour < 0 or currentHour > 23:
        return -1
    
    newHour = (currentHour + interval)%24 
    
    return newHour

#################################################
# Test Functions
#################################################

def testIsSmallFair():
    print("Testing isSmallFair...", end="")
    assert(isSmallFair(1234)) #true case
    assert(isSmallFair(-1234)) # true case
    assert(isSmallFair(15112) == False)
    assert(isSmallFair("1234") == False)
    assert(isSmallFair(1234.0) == False)
    assert(isSmallFair(-1234))  # true case
    assert(isSmallFair(1123)==False)
    assert(isSmallFair(2234)==False)
    #assert(isSmallFair(0012)==False)

    print("Passed!")

def testIsRightTriangle():
    print("Testing isRightTriangle ...")
    assert(isRightTriangle(0, 0, 3, 0, 0, 4) )  # true case
    assert(isRightTriangle(3, 0, 0, 0, 0, 4) )  # true case
    assert(isRightTriangle(0, 4, 3, 0, 0, 0) )  # true case
    assert(isRightTriangle(0, 0, 1, 1, 100, 0) == False)
    assert(isRightTriangle(0,0,5,0,0,10))  # true case
    print("passed!")
    
def testHourDifference():
    print("We need to write some testcases here!")
    print("Be sure to write them *before* writing the solution.")
    print("Try some strange things, like interval being more than 24 hours.")

    print("Testing hourDifference ...")
    assert(hourDifference(0, 24) == 0)
    assert(hourDifference (22, 3) == 1)
    assert(hourDifference (-1, 2) == -1)
    assert(hourDifference (25, 1) == -1)
    assert(hourDifference (3 , -48) == 3)
    assert(hourDifference (2, -4) == 22)

    print("Passed :")
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
