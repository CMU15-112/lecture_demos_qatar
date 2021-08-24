from turtle import *

#speed(0)
#delay(0)

# These are my variables that store information about the shape
# that I want to draw
numSides = 8
edgeLength = 100

# Draw the shape
for i in range(numSides):
    forward(edgeLength)
    left(360/numSides)
    
# Could be more code here