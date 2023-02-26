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
        s = "Hello, I'm a Circle with radius " + str(self.r)
        s += "\n" + "I'm located at " + str(self.x) + "," + str(self.y)
        return s
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        if self.r == other.r and self.x == other.x and self.y == other.y:
            return True
        return False
        
   
myCircle = Circle(5, 0, 0)
myOtherCircle = Circle(5, 0, 0)
s = str(myCircle)  # myCircle.__repr()
#if myCircle == myOtherCircle:  #myCircle.__eq__(myOtherCircle)
#    print("Great, they are the same")

if myCircle == 15112:
    print("Great, they are the same")
    

