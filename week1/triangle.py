def testIsRightTriangle():
    print("Testing isRightTriangle ...")
    assert(isRightTriangle(0, 0, 3, 0, 0, 4) )
    #assert(isRightTriangle(3, 0, 0, 0, 0, 4) )
    #assert(isRightTriangle(0, 4, 3, 0, 0, 0) )
    ##assert(isRightTriangle(0, 0, 1, 1, 100, 0) == False)
    #assert(isRightTriangle(0,0,5,0,0,10))
    print("passed!")

def distance( x1,y1,x2,y2 ):
    d = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return d

def  isRightTriangle(x1, y1, x2, y2, x3, y3):
    a = distance(x1,y1, x2,y2)
    b = distance(x1,y1, x3,y3)
    c = distance(x2,y2, x3,y3)
    print("a=", a)
    print("b=", b)
    print("c=", c)
    if math.isclose((a**2+b**2),c**2):
        return True
    if (a**2+c**2) == b**2:
        return True
    if (b**2+c**2) == a**2:
        return True
    return False


 

testIsRightTriangle()
