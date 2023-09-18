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
    for angle in range(0, 360, 30):
        angle = math.radians(angle)
        hourX = cx + smallRadius * math.cos(angle)
        hourY = cy + smallRadius * math.sin(angle)
        label = str(num)
        drawLabel(label, hourX, hourY,bold=True,size=fontSize)
        num += 1
        if num == 13:
            num = 1
        
def redrawAll(app):
    drawClockFace(app.width, app.height)  # I like helper functions!
    drawNumbers(app.width, app.height)
    
    
runApp(600, 600)