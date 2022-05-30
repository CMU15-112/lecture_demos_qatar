import math
class Circle:
    def __init__(self, radius,cx, cy): #constructor
    
        # store the data
        self.radius = radius  #storing the radius in the object itself
        self.x = cx
        self.y = cy
        self.area = math.pi * (self.radius) ** 2
    def __repr__(self):
        # should return a string representation of
        # your object
        return f"CIRCL(r={self.radius},x={self.x},y={self.y})"
    
    def __eq__(self, other):
        return isinstance(other, Circle) and \
               self.radius ==  other.radius and \
               self.x == other.x and \
               self.y == other.y
        

        
        
    def getArea(self):
        return self.area
        
myCircleA = Circle(10, 0, 0 )  # radius = 10, center (0,0)
myCircleB = Circle(5, 1, 2)  # radius = 5, center (1,2)
myList = []
myList.append(myCircleA)
myList.append(myCircleB)

a = Circle(20, 3, 4)
b = Circle(16, -4, -6)
c = Circle(20, 3, 4)

print("a is equal to b", a==b)
print("a is equal to c", a==c)  # a==c a.__eq__(c)
print("a is equal to 4", a==4)  
print("b is equal to c", b==c)






print("circleA is ", myCircleA)
print(myList)

