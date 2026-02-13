from cmu_graphics import *
import math
import random


def distance(x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2 + (y1 - y0)**2)

def reset(app):
    app.count = 0
    app.cx = app.width // 2
    app.cy = app.height // 2
    app.r = 200
    app.p = 0
    app.gameOver = False
    ## adding motion
    app.speed = 5
    app.dx = -1
    app.dy = 0
    
# This is called when the program starts
def onAppStart(app):
    reset(app)

# This is called every time one key is pressed
def onKeyPress(app, key):
    if key in "rR":
        reset(app)

# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    if distance(app.cx, app.cy, x, y) < app.r/5:
        app.p += 1
        app.r -= 50
        if app.r <= 0:
            app.r = 1
            app.gameOver = True
        #helper(app)

# This is called many times to refresh the window
def redrawAll(app):
    drawLabel(f"Points: {app.p} in {app.count/30:.2f} seconds", 
              app.width // 2, app.height // 30, size = app.width // 20)
    if app.gameOver == False:
        for i in range(5):
            if i % 2 == 0:
                color = 'red'
            else:
                color = 'white'
            r = app.r - (i * app.r / 5)
            drawCircle(app.cx, app.cy, r, fill = color)
    else:
        drawLabel(f"Game Over!  You win!", app.width // 2,
                  app.height // 2, size = app.width // 13)




# This is called "often" (def. by app.stepsPerSecond)
def onStep(app):
    if app.gameOver == False:
        app.count += 1
        app.cx += (app.speed*app.dx)
        app.cy += (app.speed*app.dy)

        if app.cy-app.r <= 0 or app.cy+app.r >= app.height:
            app.dy *= -1
            
        if app.cx - app.r <= 0 or app.cx + app.r >= app.width:
            app.dx*= -1

# This is how you run the program
runApp(width=600, height=600)
