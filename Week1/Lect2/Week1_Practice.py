import math

#################################################
# Functions (for you to write)
#################################################

# isPositiveMultipleOfFiveInt(n)
# Write the function isPositiveMultipleOfFiveInt(n)
# that takes a value n
# a returns True if n is a positive integer,
# multiple of 5, or False otherwise.
def isPositiveMultipleOfFiveInt(n):
    #if not int and not positive
    if type(n)!= int or n <= 0:
        return False
    
    #multiple of 5
    return n%5==0
    

def sideL(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
    
#Write a function getTrianglePerimeter(x1, y1, x2, y2, x3, y3) 
#which calculates and returns the perimeter of a triangle given its coordinates. 
#Hint: It might be useful to use a helper function to find side lengths.
def getTrianglePerimeter(x1, y1, x2, y2, x3, y3):
    # p = s1l + s2l+ s3l
    s1l= sideL(x1, y1, x2, y2)
    s2l= sideL(x2, y2, x3, y3)
    s3l= sideL(x1, y1, x3, y3)
    return s1l+s2l+s3l


# We will say that a value n is a small 42ish (coined term) if it is an
  #integer number with precisely four digits and has at least one pair of
  #consecutive digits that form the number 42.
  #For example, 4212, 5042, and -4242 are small 42ish numbers
  #because they are integers, have four digits, and {\bf 42} appears inside each
  #of these numbers.
  #With this in mind, and without using strings or loops,
    #write the function isSmall42ish(n) that takes a value n, 
    #which may or may not be an integer, and returns True if n is a small42ish number, 
    #and False otherwise. Do not crash if n is not an integer! Do not use strings or loops here. 
def isSmall42ish(n):
    return False


#################################################
# Test Functions
#################################################

def testIsPositiveMultipleOfFiveInt():
    print("Testing isPositiveMultipleOfFiveInt...", end="")
    assert(isPositiveMultipleOfFiveInt(5)) # True case
    assert(isPositiveMultipleOfFiveInt(-5) == False)
    assert(isPositiveMultipleOfFiveInt("five") == False)
    assert(isPositiveMultipleOfFiveInt(5.0) == False)
    print("Passed !")

def testGetTrianglePerimeter():
    assert(getTrianglePerimeter(0, 0, 3, 0, 0, 4)==12)  
    assert(getTrianglePerimeter(3, 0, 0, 0, 0, 4)==12)  
    assert(getTrianglePerimeter(0, 4, 3, 0, 0, 0)==12 )  
    assert(getTrianglePerimeter(0, 0, 1, 1, 100, 0)== 200.4192639386039)
    assert(getTrianglePerimeter(0,0,5,0,0,10)== 26.18033988749895)
    print("passed!")

    

def testIsSmall42ish():
    print("Write your own test cases")


#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testIsPositiveMultipleOfFiveInt()
    testGetTrianglePerimeter()
    #testIsSmall42ish()

def main():
    testAll()

if __name__ == '__main__':
    main()