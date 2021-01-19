from turtle import *

def drawShape(edgeLength, numSides):
    for i in range(numSides):
        forward(edgeLength)
        left(360/numSides)

for i in range(4):
    drawShape(50, 4)
    forward(100)