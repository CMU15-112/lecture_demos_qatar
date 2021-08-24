from turtle import *

#speed(0)
#delay(0)

def drawShape(edgeLength, numSides):
    for i in range(numSides):
        forward(edgeLength)
        left(360/numSides)
        
drawShape(100,4)
penup()
#left(180)
#forward(50)
#left(180)

#backward(50)

forward(-50)

pendown()
drawShape(200,5)
