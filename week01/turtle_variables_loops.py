from turtle import *

# Some variables
edge = 1
numSides = 800

# Draw one side of a square four times
for i in range(numSides):
    forward(edge)
    left(360/numSides)