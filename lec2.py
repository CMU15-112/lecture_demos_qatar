import turtle
def drawOctagon(x):
    for n in range(8):
        turtle.forward(x)
        turtle.left(45)

def drawSquare(size):
    for n in range(4):
        turtle.forward(size)
        turtle.left(90)



turtle.delay(0)
def drawFlower():
    turtle.forward(50)
    turtle.backward(25)
    turtle.left(110)
    turtle.circle(-400,40)
    turtle.right(80)
    turtle.circle(10)
drawFlower()

##for p in range(4):
##    drawOctagon(40)
##    turtle.pu()
##    turtle.forward(83)
##    turtle.pd()
##
##drawOctagon(10)
