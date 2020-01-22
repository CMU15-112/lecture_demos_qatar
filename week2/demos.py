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
    
print(circlesIntersect(0,0,1,5,5,3))
    