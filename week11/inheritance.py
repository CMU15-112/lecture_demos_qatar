import math


class GeometricFigure:
    pass

class Rectangle(GeometricFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = "red"
        self.outlineColor =  "black"

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

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    def mySpecialPropertyOnlyForSquares(self):
        pass




rect1 = Rectangle(10, 10)

square1 = Square(10)

print(isinstance(rect1, Rectangle))
print(isinstance(square1, Rectangle))
print(isinstance(rect1, Square))
print(isinstance(rect1, GeometricFigure))
print(isinstance(square1, GeometricFigure))

shape = GeometricFigure()
