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
        
myCircle = Circle(5, 0, 0)
myOtherCircle = Circle(10, 0, 0)

print("The area is=", myCircle.getArea())
s = str(myCircle)
print(type(s))
print(s)






        
        
    