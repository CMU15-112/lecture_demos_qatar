from turtle import *

numSides = 8
sideLength = 100

angle = 360 / numSides

for n in range(numSides):
    forward(sideLength)
    left(angle)
