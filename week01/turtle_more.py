from turtle import *

def drawFlower(numPetals, radius):
    for n in range(numPetals):
        circle(radius)
        right(360/numPetals)

def drawDashedCircle(numDashes):
    for n in range(numDashes):
        penup()
        circle(50, 360/(2*numDashes))
        pendown()
        circle(50, 360/(2*numDashes))
       
speed(0)
drawDashedCircle(50)
