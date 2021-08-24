from turtle import *

def drawShape(edgeLength, numSides, shapeColor):
    color(shapeColor)
    begin_fill()
    for i in range(numSides):
        forward(edgeLength)
        left(360/numSides)
    end_fill()
        
def drawBase():
    forward(50)
    forward(-25)
    left(90)
    forward(150)
    
drawBase()
right(30)
drawShape(50, 3, "blue")
left(120)
drawShape(50, 3, "red")
left(120)
drawShape(50,3, "green")
