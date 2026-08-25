import math

# My Functions

# Calculate the distance between the point (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def testDistance():
    print("Testing distance....", end="")
    assert math.isclose(5, distance(0,0,4,3))
    assert math.isclose(2 ** 0.5, distance(0, 0, 1, 1))
    assert math.isclose(333 ** 0.5, distance(7, 4, 25, 7))
    print("done")
    
testDistance()