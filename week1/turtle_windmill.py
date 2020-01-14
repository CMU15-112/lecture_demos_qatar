from turtle import *

def drawBase():
    forward(100)
    left(180)
    forward(50)
    right(90)
    forward(200)

def drawTriangle():
    for n in range(3):
        forward(50)
        left(120)
    

drawBase()
left(90)
drawTriangle()
right(240)
drawTriangle()
left(120)
drawTriangle()