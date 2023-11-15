import math

class Circle:
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    def getArea(self):
        area = math.pi * (self.r ** 2)
        return area
    def __repr__(self):
        return f"CIR[r:{self.r}]@{(self.x,self.y)}"
    def __eq__(self, other):
        if isinstance(other, Circle) and \
           self.r == other.r and self.x == other.x and self.y == other.y:
            return True
        return None

        #return False



cA = Circle(5, 0, 0)
cB = Circle(10, 0, 0)

#print(cA, cB)

cC = Circle(5, 0, 0)

#assert(cA == cC)
print(cA != cB)
#assert(cA != cB)
#assert(None)

hello = "42"
assert(hello != cA)


print("All tests passed")
