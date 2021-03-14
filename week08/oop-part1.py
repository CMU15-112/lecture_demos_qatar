import math

class Circle(object):
    # Store x, y, r about a circle
    def __init__(self, r, x, y):        
        self.radius = r
        self.x = x
        self.y = y
    
#     def __str__(self):
#         return f"Circle(r={self.radius},x={self.x},y={self.y})"
    
    def __repr__(self):
        return f"Circle(r={self.radius},x={self.x},y={self.y})"
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius \
               and self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return hash( (self.radius, self.x, self.y) )
    
    def getArea(self):
        return math.pi * (self.radius) ** 2
    

myCircle = Circle(5, 0, 0)
myOtherCircle = Circle(10, 0, 0)

# # You can do this, but probably shouldn't.
# myCircle.radius = 6

print(myCircle.getArea())
print(myOtherCircle.getArea())

print("---")
print(myCircle)
myList = []
myList.append(myCircle)
myList.append(myOtherCircle)
print(myList)

print("---")
a = Circle(20, 3, 4)
b = Circle(16, -4, -6)
c = Circle(20, 3, 4)
d = Circle(2*10, 3, 4)

print(a == b) # Translates to... a.__eq__(b)
print(b == a) # Translates to... b.__eq__(a)
print(b == c)
print(a == c)
print(a == d)
print(a == "Monkey")

print("---")
mySet = set()
mySet.add(a)
mySet.add(b)
mySet.add(Circle(20, 3, 16))
print(mySet)

print(c in mySet)
print(d in mySet)
print(Circle(20, 3, 5) in mySet)