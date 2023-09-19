from cmu_graphics import *
import math
import random


def onAppStart(app):
    app.counter = 0
    app.radius = 40 
    app.cx = app.width//2
    app.cy = app.height//2

def onMousePress(app, x, y):
    if (app.cx - x) ** 2 + (app.cy - y) **2 <= (app.radius/5)**2:
        app.counter += 1
        
        
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