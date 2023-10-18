from cmu_graphics import *
import math

# the clock as we did it in class
def redrawAll(app):
    cx = app.width//2
    cy = app.height//2
    r = app.width//4
    drawCircle(cx, cy, r, fill="yellow")

    initAngle = 60
    for i in range(1,13):
        px = cx + 0.8*r*math.cos(math.radians(initAngle))
        py = cy - 0.8*r*math.sin(math.radians(initAngle))
        drawLabel(f"{i}", px, py, size=0.05*app.height)
        initAngle-=30
        

runApp(800, 800)