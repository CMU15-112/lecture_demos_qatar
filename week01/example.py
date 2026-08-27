import math

# My Functions

def rectanglesOverlap(left1, top1, w1, h1, left2, top2, w2, h2):
    pass

# Calculate the distance between the point (x1, y1) and (x2, y2)
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def testRectanglesOverlap():
    print("Testing rectanglesOverlap....", end="")
    # L, S
    assert rectanglesOverlap(7, 4, 10, 7, 5, 6, 3, 3) == True
    # U, S
    assert rectanglesOverlap(7, 4, 10, 7, 10, 2, 3, 3) == True
    # R, S
    assert rectanglesOverlap(7, 4, 10, 7, 15, 6, 3, 3) == True
    # D, S
    assert rectanglesOverlap(7, 4, 10, 7, 9, 10, 3, 3) == True
    # Corners
    assert rectanglesOverlap(7, 4, 10, 7, 5, 2, 3, 3) == True
    assert rectanglesOverlap(7, 4, 10, 7, 16, 2, 3, 3) == True
    assert rectanglesOverlap(7, 4, 10, 7, 16, 10, 3, 3) == True
    assert rectanglesOverlap(7, 4, 10, 7, 5, 10, 3, 3) == True 
    # Bigger
    assert rectanglesOverlap(7, 4, 10, 7, 5, 1, 13, 13) == True
    
    # Non-overlapping
    assert rectanglesOverlap(7, 4, 10, 7, 1, 5, 4, 4) == False
    assert rectanglesOverlap(7, 4, 10, 7, 10, 1, 2, 2) == False
    assert rectanglesOverlap(7, 4, 10, 7, 18, 5, 2, 2) == False
    assert rectanglesOverlap(7, 4, 10, 7, 10, 20, 2, 2) == False



    ## Mirror all test cases above, and swap rectangle 1 and rectangle 2 ##
    

    
    print("done")


def testDistance():
    print("Testing distance....", end="")
    assert math.isclose(5, distance(0,0,4,3))
    assert math.isclose(2 ** 0.5, distance(0, 0, 1, 1))
    assert math.isclose(333 ** 0.5, distance(7, 4, 25, 7))
    print("done")
    
testDistance()
testRectanglesOverlap()
