import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getArea(self):
        area = self.width * self.height
        return area
    def __repr__(self):
        s = f"Hello, I'm a Rectangle with w: {self.width} and h: {self.height}"
        return s
    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        if self.width == other.width and self.height == other.height:
            return True
        return False
        

class Square(Rectangle):  # A square is a rectangle with equal width and height
    def __init__(self, side):  # rewrite the constructor to use a single parameter
        super().__init__(side, side)  # call the parent's constructor
    def __repr__(self):
        s = f"Hello, I'm a Square with side: {self.width}"
        return s
    
r1 = Rectangle(10, 5)
print(r1)
r2 = Rectangle(5, 5)
print(r2)
sq1 = Square(5)
print(sq1)
print(r1 == sq1)
print(r2 == sq1)  # they are mathematically the same polygon




