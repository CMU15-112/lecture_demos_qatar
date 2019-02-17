import math

def distance(x1, y1, x2, y2):
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return d
    
# Return true if the two circles intersect, and false otherwise.
def circlesIntersect(x1, y1, r1, x2, y2, r2):
    distanceBetweenCircles = distance(x1,y1,x2,y2)
    if distanceBetweenCircles <= (r1+r2):
        return True
    else:
        return False
    
# Returns the 1s digit of n
# If n isn't a number, return None
def onesDigit(n):
    if not ((type(n) == int) or (type(n) == float)):
        return None
        
    n = abs(n)
    answer = int(n)%10
    return answer
    
def hundredsDigit(n):
    if not ((type(n) == int) or (type(n) == float)):
        return None
        
    return onesDigit(abs(n)//100)
    
def testDistance():
    print("Testing testDistance...",end="")
    assert(math.isclose(distance(0,0,1,1), 2**0.5))
    assert(math.isclose(distance(7,4,25,7), 333**0.5))
    assert(math.isclose(distance(3,3,-3,-3), 6*2**0.5))
    print("pass.")
    
def testCirclesIntersect():
    print("Testing testCirclesIntersect...",end="")
    assert(circlesIntersect(0,0,2,2,0,2) == True)
    assert(circlesIntersect(0,0,2,4,0,2) == True)
    assert(circlesIntersect(0,0,2,5,0,2) == False)
    print("pass.")
    
def testOnesDigit():
    print("Testing onesDigit...", end="")
    assert( onesDigit(8926) ==  6 )
    assert( onesDigit(2*2) ==  4 )
    assert( onesDigit(0) ==  0 )
    assert( onesDigit(892.6) ==  2 )
    assert( onesDigit(-8926) ==  6 )
    assert( onesDigit("This isn't a number") == None )
    assert( onesDigit(None) == None )
    print("pass.")
 
def testHundredsDigit():
    print("Testing hundredsDigit...", end="")
    assert( hundredsDigit(8926) ==  9 )
    assert( hundredsDigit(2*2) ==  0 )
    assert( hundredsDigit(0) ==  0 )
    assert( hundredsDigit(892.6) ==  8 )
    assert( hundredsDigit(7523892.6) ==  8 )
    assert( hundredsDigit(-8926) ==  9 )
    assert( hundredsDigit("This isn't a number") == None )
    assert( hundredsDigit(None) == None )
    print("pass.")   
    
testDistance()
testCirclesIntersect()
testOnesDigit()
testHundredsDigit()