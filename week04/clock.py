import math
from cmu_graphics import *

def drawClockFace(app):
    cx = app.width/2
    cy = app.height/2
    smaller = min(app.width, app.height)
    print(smaller)
    r = 0.9 * (smaller/2)
    drawCircle(cx, cy, r, fill=None, border="black")
    
    numRadius = r * 0.9
    
    for i in range(1, 13):
        angle = (360/12)*i
        angleRadians = math.radians(angle)
        dx = numRadius * math.sin(angleRadians)
        dy = numRadius * math.cos(angleRadians)
        #drawCircle(cx+dx, cy-dy, 5)
        drawLabel(str(i), cx+dx, cy-dy, size=smaller//20)

def redrawAll(app):
    drawClockFace(app)

runApp(width=800, height=600)
