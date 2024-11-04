import math

class Circle:
    
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
    
    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def getCircumference(self):
        return 2 * math.pi * self.radius
    
    # Distance from (x,y) to the edge of this circle
    def distanceFrom(self, x, y):
        return abs(((self.x-x)**2 + (self.y-y)**2)**0.5 - self.radius)
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius and \
               self.x == other.x and self.y == other.y
    
    #def __str__(self):
    #    return f"Circle({self.radius}, {self.x}, {self.y})"
    
    def __repr__(self):
        return f"Circle({self.radius}, {self.x}, {self.y})"
    
    def __hash__(self):
        return hash( (self.radius, self.x, self.y) )

c = Circle(5, 1, 3)
print(c.radius)
print(c.getArea())
print(c.getCircumference())
print(c.distanceFrom(1.5, 3.5))
print(type(c))

c2 = Circle(10, 50, 60)
print(c2.radius)
print(c.radius)

c3 = Circle(5, 1, 3)

print(c.__eq__(c2))
print(c == c2)
print(c == c3)
print(c == 5.0)

print(c)
print(c2)
print(c3)

L = [[c, c2, c3], [c]]
print(L)

print(str(c))

s = set()
s.add(c)
s.add(c2)
s.add(c3)
print(s)

c2.radius = 67
print(s)
print(c2 in s)

c4 = Circle(10, 50, 60)
print(c4 in s)

