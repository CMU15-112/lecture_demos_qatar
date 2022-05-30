# Let's create an object that represents a Circle

# myCircle.getArea()
# myCircle wil have type Circle
import math

class SimpleCircle:
     def __init__(self, radius):
         self.radius = radius
        
class Circle:
    def __init__(self, radius,cx, cy): #constructor
    
        # store the data
        self.radius = radius  #storing the radius in the object itself
        self.center_x = cx
        self.center_y = cy
        
    def getArea(self):
        return math.pi * (self.radius) ** 2
        
myCircleA = Circle(10, 0, 0 )  # radius = 10, center (0,0)
myCircleB = Circle(5, 1, 2)  # radius = 5, center (1,2)

print("CircleA area = ", myCircleA.getArea()) #calling getArea
print("CircleB area = ", myCircleB.getArea())

anotherCircle = SimpleCircle(20)
print(type(anotherCircle))
print(type(myCircleA))
# reading class variable radius
print("the radius of myCircleA is ", myCircleA.radius)
print("the radius of anotherCircle is ", anotherCircle.radius)


def anotherGetArea(mycircle):
    # check what's the type that was given
    
    # assuming mycircle is of type Circle
    # therefore, I can get the radius with mycircle.radius
    # we can access data outside the class
    return math.pi * (mycircle.radius) ** 2


print(type(myCircleA))
print(type(myCircleB))

    


