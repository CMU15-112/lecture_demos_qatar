from cmu_graphics import *
import math


def drawClockFace(app, cx, cy, radius, color='yellow'):
    drawCircle(cx,cy,radius, fill=color)
    
def drawNumbers(app, cx, cy, radius):
    smallRadius = 0.85*radius
    num = 3
    fontSize = radius//6
    # approach: start from 3  -> 3 corresponds to angle 0 with inverted axes
    for angle in range(0, 360, 30):
        angle = math.radians(angle)
        hourX = cx + smallRadius * math.cos(angle)
        hourY = cy + smallRadius * math.sin(angle)
        label = str(num)
        drawLabel(label, hourX, hourY,bold=True,size=fontSize)
        num = num%12 + 1
    
def drawWallClock(app):
    radius = app.width//4
    cx, cy = app.width//2, app.height//2
    #drawClockFace(app, cx, cy, radius)
    drawNumbers(app, cx, cy, radius)
    #drawHands(app, cx, cy, radius)
   
    
def redrawAll(app):
    drawWallClock(app)
    
    
runApp(600, 600)