from cmu_graphics import *
import math
import random

def distance(x0, y0, x1, y1):
    return math.sqrt((x1-x0)**2 + (y1 - y0)**2)

def moveTarget(app):
    app.cx = random.randint(app.radius, app.width - app.radius)
    app.cy = random.randint(app.radius, app.height - app.radius)

def reset(app):
    app.count = 0
    app.cx = app.width // 2
    app.cy = app.height // 2
    app.radius = 150
    app.points = 0
    app.gameOver = False
# This is called when the program starts
def onAppStart(app):
    reset(app)

# This is called every time one key is pressed
def onKeyPress(app, key):
    if key in "rR":
        reset(app)

# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    if distance(app.cx, app.cy, x, y) < app.radius/5:
        app.points += 1
        app.radius -= 100
        if app.radius <= 0:
            app.radius = 1
            app.gameOver = True
        moveTarget(app)

# This is called many times to refresh the window
def redrawAll(app):
    drawLabel(f"Points: {app.points} in {app.count/30:.2f} seconds", app.width // 2, app.height // 30, size = app.width // 20)
    if app.gameOver == False:
        for i in range(5):
            if i % 2 == 0:
                color = 'red'
            else:
                color = 'white'
            r = app.radius - (i * app.radius / 5)
            drawCircle(app.cx, app.cy, r, fill = color)
    else:
        drawLabel(f"Game Over!  You win!", app.width // 2, app.height // 2, size = app.width // 13)

# This is called "often" (def. by app.stepsPerSecond)
def onStep(app):
    if app.gameOver == False:
        app.count += 1

# This is how you run the program
runApp(width=800, height=800)


