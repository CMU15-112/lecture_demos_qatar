class Rectangle:
    def __init__(self, width , height):
        self.width = width
        self.height = height
    def __repr__(self):
        #print("__repr__ is being called")
        return f'REC: {self.width} {self.height}'
    def area(self):
        return self.width * self.height
    

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        
    
    
r1 = Rectangle(10, 5)
r2 = Rectangle(5, 5)
assert str(r1) == "REC: 10 5"

sq1 = Square(5)
assert isinstance(sq1, Square)  
assert isinstance(sq1, Rectangle)

assert sq1.area() == 25

print("Passed :)")