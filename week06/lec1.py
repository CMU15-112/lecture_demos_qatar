from cmu_graphics import *
import math
import random


def onAppStart(app):
    app.counter = 0
    app.radius = 40
    app.cx = app.width//2
    app.cy = app.height//2
    app.points = 0

def onStep(app):
    app.counter += 1
    
    if app.counter % 30 == 0:
        app.cx = random.randint(app.radius, app.width - app.radius)
        app.cy = random.randint(app.radius, app.height - app.radius)

def onMousePress(app, x, y):
    d = math.sqrt((x - app.cx) ** 2 + (y - app.cy) ** 2)
    if d < app.radius:
        app.radius = max(1, app.radius - 1)
        if app.radius > 1:
            app.points += 1


def drawTarget(app, x, y, r):
    for i in range(5):
        if i%2 == 0:
            color = 'red'
        else:
            color = 'white'
        tempR = r - (i * r / 5)
        drawCircle(x, y, tempR,fill=color)    

def redrawAll(app):
    drawTarget(app, app.cx, app.cy, app.radius)
    drawLabel(f"{app.points} points", app.width // 2, 20, size=20)

runApp(width=800, height=800)
