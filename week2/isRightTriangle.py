""" isRightTriangle
Check if the triangle defined by points (x1,y1) (x2,y2) (x3,y3) is a right triangle. 
Return True if the triangle is right-angled, False otherwise
"""
import math

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def isRightTriangle(x1, y1, x2, y2, x3, y3):
    side12 = distance(x1, y1, x2, y2)
    side13 = distance(x1, y1, x3, y3)
    side23 = distance(x2, y2, x3, y3)
#    print("side12:", side12)
#    print("side13:", side13)
#    print("side23:", side23)
    # side12 is the larger
    if side12 >= side13 and side12 >= side23:
        return math.isclose(side12**2, side13**2 + side23**2)
    # side13 is the larger
    if side13 >= side12 and side13 >= side23:
        return math.isclose(side13**2,side12**2 + side23**2)
    # side23 is the larger
    if side23 >= side13 and side23 >= side12:
        return math.isclose(side23**2,side13**2 + side12**2)
    
    
def testIsRightTriangle():
    print("Testing isRightTriangle ...")
    assert(isRightTriangle(0, 0, 3, 0, 0, 4) )
    assert(isRightTriangle(3, 0, 0, 0, 0, 4) )
    assert(isRightTriangle(0, 4, 3, 0, 0, 0) )
    assert(isRightTriangle(0, 0, 5, 5, 100, 0) == False)
    assert(isRightTriangle(0,0,5,0,0,10))
    print("passed!")
    
testIsRightTriangle()
#isRightTriangle(0, 0, 3, 0, 0, 4)
    