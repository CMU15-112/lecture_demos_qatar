import math

class Circle:
    def __init__(self, a=0, b=0, rad=42):
        self.x = a
        self.y = b
        self.radius = rad
        print("I'm inside __init__")
    def area(self):
        print("Computing area ....")
        return math.pi * (self.radius ** 2)
    def __repr__(self):
        return f'this is circle @ ({self.x}, {self.y}) has radius {self.radius}'
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius \
               and self.x == other.x and self.y == other.y
    
                
# create a circle (42,25) with radius 20
#c = [42,25,20]
c1 = Circle(42,25,20)
c2 = Circle()
c3 = Circle(42,25,20)
c4 = c1

print

print(c1.area())
print(c2.area())

if "hello" == c1:
    print("this is bad")
if c1 == c4:
    print("circles are equal")
    
print(f'Circle 1 is {c1}')
print("string " + str(c1))


print(c1 in [c1,c2])

             

#c.x = 42
#c.y = 25
#c.radius = 20
# do some stuff  not related to circle
# update the position to (42,42)
#c.y += 1
#print(c.y)

