from cmu_graphics import *
import math


def drawClockFace(width, height):
    radius = min(width, height)//4
    cx, cy = width//2, height//2
    drawCircle(cx,cy,radius, fill="yellow")
    
def drawNumbers(width, height):
    radius = min(width, height)//4
    smallRadius = 0.85*radius
    cx, cy = width//2, height//2
    num = 3
    fontSize = min(width,height)//24
    # approach: start from 3  -> 3 corresponds to angle 0 with inverted axes
    for angle in range(0, 360, 30):
        angle = math.radians(angle)
        hourX = cx + smallRadius * math.cos(angle)
        hourY = cy + smallRadius * math.sin(angle)
        label = str(num)
        drawLabel(label, hourX, hourY,bold=True,size=fontSize)
        num = num%12 + 1
        
def redrawAll(app):
    drawClockFace(app.width, app.height)
    drawNumbers(app.width, app.height)
    
    
runApp(600, 600)