from cmu_graphics import *
import math
from datetime import datetime

def calcPointFromAngle(theta, r, cx, cy):
    dx = r * math.sin(theta)
    dy = r * math.cos(theta)
    nx = cx + dx
    ny = cy - dy
    return nx, ny

def drawClock(app, cx, cy, hour, minute, second):
    # Minimum window width/height
    sizeFactor = min(app.width, app.height)
    
    # Draw the circle
    r = 0.9 * min(app.width, app.height)//2
    drawCircle(cx, cy, r, fill="white", border="black")
    rn = 0.87 * r
    
    # Draw the numbers
    for i in range(1, 13):
        theta = i * (2 * math.pi / 12)
        nx, ny = calcPointFromAngle(theta, rn, cx, cy)
        drawLabel(str(i), nx, ny, size=sizeFactor/20)
        
    # Draw Ticks
    for i in range(60):
        theta = i * (2 * math.pi / 60)
        endX, endY = calcPointFromAngle(theta, r, cx, cy)

        theta = i * (2 * math.pi / 60)
        startX, startY = calcPointFromAngle(theta, 0.95*r, cx, cy)
        
        if i % 5 == 0:
            thickness = 5 * sizeFactor / 800
        else:
            thickness = sizeFactor / 800
        
        drawLine(startX, startY, endX, endY, lineWidth=thickness)
    
    # Draw Hands
    minute = minute + (second/60)
    hour = hour + (minute/60)
    theta = hour * (2 * math.pi / 12)
    hourX, hourY = calcPointFromAngle(theta, 0.5 * r, cx, cy)
    drawLine(cx, cy, hourX, hourY, lineWidth=5 * sizeFactor/800)
    
    theta = minute * (2 * math.pi / 60)
    minuteX, minuteY = calcPointFromAngle(theta, 0.65 * r, cx, cy)
    drawLine(cx, cy, minuteX, minuteY, lineWidth=3 * sizeFactor/800)

    theta = second * (2 * math.pi / 60)
    secondX, secondY = calcPointFromAngle(theta, 0.76 * r, cx, cy)
    drawLine(cx, cy, secondX, secondY, lineWidth=2 * sizeFactor/800)   

def redrawAll(app):
    now = datetime.now()
    drawClock(app, app.width//2, app.height//2, now.hour, now.minute, now.second)

runApp(800,800)