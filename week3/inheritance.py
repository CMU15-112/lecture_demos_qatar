import math
class Ellipse:  # I can omit (object)
    # Store x, y, r about a circle
    def __init__(self, w, h, x, y):        
        self.width = w
        self.height = h
        self.x = x
        self.y = y
        
    def getArea(self):
        print("I'm the ellipse parent")
        self.area = math.pi * self.width * self.height
        return math.pi * self.width * self.height

class Circle(Ellipse):  #Circle is a child of Ellipse
    def __init__(self, r, x, y):
        super().__init__(r, r, x, y)
#    def getArea(self):
#        print("Computing area of a circle")
#        area = super().getArea()
#        return self.area
    
    
        
myCircleA = Circle(10, 0, 0 )  # radius = 10, center (0,0)
myCircleB = Circle(5, 1, 2)  # radius = 5, center (1,2)

print(type(myCircleA) == Circle)
print(type(myCircleA) == Ellipse)

print(isinstance(myCircleA, Circle))
print(isinstance(myCircleA, Ellipse))

print(myCircleA.getArea())


#print("CircleA area = ", myCircleA.getArea()) #calling getArea
#print("CircleB area = ", myCircleB.getArea())
        

        