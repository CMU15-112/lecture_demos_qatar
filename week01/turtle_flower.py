from turtle import *

def drawSquare(length):
    for n in range(4):
        forward(length)
        left(90)

def drawFlower(numPetals, lengthOfSide):
    for n in range(numPetals):
        drawSquare(lengthOfSide)
        right(360/numPetals)

color("blue")
speed(0)
drawFlower(60, 200)