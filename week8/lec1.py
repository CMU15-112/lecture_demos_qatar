import math

class Circle(object):
    
    def __init__(self, r, x, y):
        self.radius = r
        self.x = x
        self.y = y
        
    #def __str__(self):
    #    return "Circle with radius " + str(self.radius)
    
    def __repr__(self):
        return "Circle with radius " + str(self.radius)
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius \
               and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash( (self.radius, self.x, self.y) )
        
    def getArea(self):
        return math.pi * (self.radius ** 2)

class Hexagon(object):
    
    def __init__(self, s):
        self.side = s
        
    def getArea(self):
        return (3 * math.sqrt(3) * self.side ** 2)/2
    
    def __repr__(self):
        return "Hexagon with side " + self.side
    
    def __eq__(self, other):
        return isinstance(other, Hexagon) and self.side == other.side

# Write classes for...
# Rectangle
# Square
# Hexagon

L = []
L.append(Circle(5, 0, 0))
L.append(Circle(8, 1, 1))

for circ in L:
    print(circ)
    print(circ.radius)
    print(circ.getArea())
    
print(L)

c1 = Circle(10, 0, 0)
c2 = Circle(10, 0, 0)
c3 = Circle(20, 0, 0)
print(c1 == c2) # c1 == c2 translates into... c1.__eq__(c2)
print(c1 == c3)
print(c1 == "cat")

print(isinstance(c1, Circle))

mySet = set()
mySet.add(c1)
mySet.add(c2)
mySet.add(c3)