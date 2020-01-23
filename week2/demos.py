import math

# Calculate the distance between (x1,y1) and (x2,y2)
def distance(x1, y1, x2, y2):
    d = ( (y2-y1)**2 + (x2-x1)**2 ) ** 0.5
    return d

def testDistance():
    print("Testing distance...", end="")
    val = distance(0,0,3,4)
    if val != 5:
        print("Distance is broken")
        
    val = distance(7,4,25,7)
    if val != 333**0.5:
        print("Distance is broken")
    print("done.")
    
def testDistanceAgain():
    print("Testing distance...", end="")
    assert( math.isclose(distance(0,0,3,4),5) )
    assert( math.isclose(distance(7,4,25,7),333**0.5) )
    print("done.")

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1,y1,x2,y2)
    if r1+r2 < d:
        return False
    else:
        return True

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
    #getOnesDigit("Hi there bob")
    print("done.")

def getOnesDigit(n):
    # I should check that n is an int or a float...
    a = int(n)
    b = abs(a)
    return b % 10
    
def getHundredsDigit(n):
    a = int(n)
    b = abs(a)
    c = b % 1000
    return c // 100

def getHundredsDigit(n):
    a = int(n)
    b = abs(a)
    c = b // 100
    return c % 10
    
testDistanceAgain()
testCirclesIntersect()
testGetOnesDigit()
    