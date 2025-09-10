"""
Write the function isRightTriangle(x1, y1, x2, y2, x3, y3)
that takes 6 integers representing the coordinates of
3 points in the plane: (x1, y1), (x2, y2), (x3, y3).
These are the vertices of a triangle.

Return True if the triangle formed by these three points is a right triangle
(has one 90-degree angle), and False otherwise.
You may assume the points are distinct and not collinear.
"""

def distance( x1,y1,x2,y2 ):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    a = distance(x1,y1, x2,y2)
    b = distance(x1,y1, x3,y3)
    c = distance(x2,y2, x3,y3)
    print("a=", a)
    print("b=", b)
    print("c=", c)
    print("--------------")
    # c is the longest?
    if math.isclose((a**2+b**2), c**2):
        return True
    # b is the longest?
    if math.isclose((a**2+c**2), b**2):
        return True
    # a is the longest?
    if math.isclose((b**2+c**2), a**2):
        return True
    return False
    
    
def testIsRightTriangle():
    print("Testing isRightTriangle ...")
    assert(isRightTriangle(0, 0, 3, 0, 0, 4) )
    assert(isRightTriangle(-3, 0, 0, 0, 0, 4))
    assert(isRightTriangle(0, 0, 5, 2, 3, 0) == False)
    print("passed!")
    
testIsRightTriangle()