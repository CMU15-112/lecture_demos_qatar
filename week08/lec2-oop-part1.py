import math

class Circle(object):
    
    def __init__(self, r, x, y):
        self.radius = r
        self.x = x
        self.y = y
        print("Finished init")
        
    #def __str__(self):
    #    return f"Circle({self.radius}, {self.x}, {self.y})"
    
    def __repr__(self):
        return f"Circle({self.radius}, {self.x}, {self.y})"
        
    def getArea(self):
        return math.pi * self.radius ** 2
    
    def getCircumference(self):
        return math.pi * 2 * self.radius

c = Circle(5,1,2)
anotherC = Circle(10,5,3)

print(c.radius, c.x, c.y)
print(c.getArea())

print(anotherC.radius, anotherC.x, anotherC.y)
print(anotherC.getArea())

print(c)
print(anotherC)

L = [c, anotherC]
print(L)