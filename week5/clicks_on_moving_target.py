from cmu_graphics import *
import math
import random

def moveTarget(app):
    app.cx = random.randint(app.radius, 
        app.width - app.radius)
    app.cy = random.randint(app.radius, 
        app.height - app.radius)

def onAppStart(app):
    app.counter = 0
    app.radius = 40 
    moveTarget(app)

def onMousePress(app, x, y):
    if (app.cx - x) ** 2 + (app.cy - y) **2 <= (app.radius/5)**2:
        app.counter += 1
        moveTarget(app) # change the location of the target
        
def redrawAll(app):
    drawLabel(f'{app.counter} clicks on the target', 
        app.width//2, 100, size=20, bold=True)
    for i in range(5):
        if i%2 == 0:
            color = 'black'
        else:
            color = 'white'
        r = app.radius - (i * app.radius / 5)
        drawCircle(app.cx, app.cy, r,fill=color)

runApp(width=800, height=800)