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
    
    #reject not int
    if type(n) != int: #another way: not (type(n) == int)
        return False
    
    # reject not positive
    if n < 0 :
        return False
    
    ### another way
    # if type(n) != int or n <0:
       # return False
    
    # reject not multipple of 5
    if n%5 != 0:
        return False
    
    return True

    
#Write a function getTrianglePerimeter(x1, y1, x2, y2, x3, y3) 
#which calculates and returns the perimeter of a triangle given its coordinates. 
#Hint: It might be useful to use a helper function to find side lengths.
def getTrianglePerimeter(x1, y1, x2, y2, x3, y3):
    la = sideL(x1, y1, x2, y2)
    lb = sideL(x2, y2, x3, y3)
    lc = sideL(x1, y1, x3, y3)
    return la+lb+lc

def sideL(x1, y1, x2, y2):
    return ((x2-x1)**2+(y2-y1)**2)**0.5

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
    
    #reject not int
    if not isinstance(n, int):
        return False
    
    #reject not 4 digits
    n = abs(n)
    if n< 1000 or n > 9999:
        return False
        
    
    # reject if no two consective digits = 42
    d10 = n%100
    d32 = n//100
    d21 = (n//10)%100
    
    return (d10==42 or d32==42 or d21 == 42)


#################################################
# Test Functions
#################################################

def testIsPositiveMultipleOfFiveInt():
    print("Testing isPositiveMultipleOfFiveInt...", end="")
    assert(isPositiveMultipleOfFiveInt(5)) # True case
    assert(isPositiveMultipleOfFiveInt(0) == True) # True case
    assert(isPositiveMultipleOfFiveInt(-5) == False)
    assert(isPositiveMultipleOfFiveInt("five") == False)
    assert(isPositiveMultipleOfFiveInt(5.0) == False)
    assert(isPositiveMultipleOfFiveInt(24) == False)
    print("Passed !")

def testGetTrianglePerimeter():
    assert(getTrianglePerimeter(0, 0, 3, 0, 0, 4)==12)  
    assert(getTrianglePerimeter(3, 0, 0, 0, 0, 4)==12)  
    assert(getTrianglePerimeter(0, 4, 3, 0, 0, 0)==12 )  
    assert(getTrianglePerimeter(0, 0, 1, 1, 100, 0)== 200.4192639386039)
    assert(getTrianglePerimeter(0,0,5,0,0,10)== 26.18033988749895)
    print("passed!")

    

def testIsSmall42ish():
    assert(isSmall42ish(1234)==False)
    assert(isSmall42ish(1425) == True)
    assert(isSmall42ish(4242))
    assert(isSmall42ish("Hello")==False)
    assert(isSmall42ish(4.2)==False)
    assert(isSmall42ish(-4242))
    assert(isSmall42ish(1)==False)
    assert(isSmall42ish(12345)==False)

    print("Passed :)")


#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testIsPositiveMultipleOfFiveInt()
    testGetTrianglePerimeter()
    testIsSmall42ish()

def main():
    testAll()

if __name__ == '__main__':
    main()