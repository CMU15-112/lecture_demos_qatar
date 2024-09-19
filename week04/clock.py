import math
from cmu_graphics import *

def drawClockHands(app, hour, minute):
    if hour >= 24 or minute >= 60 or hour < 0 or minute < 0 or \
       type(hour) is not int or type(minute) is not int:
        return
    cx = app.width/2
    cy = app.height/2
    smaller = min(app.width, app.height)
    #print(smaller)
    r = 0.9 * (smaller/2)
    
    totalMinutes = hour * 60 + minute
    
    # totalMinutes * ratio of degrees per minute
    hourAngle = totalMinutes * 360 / (12 * 60)
    angleRadians = math.radians(hourAngle)
    dx =  0.45 * r * math.sin(angleRadians)
    dy =  0.45 * r * math.cos(angleRadians)
    drawLine(cx, cy, cx+dx, cy-dy, fill="black", lineWidth=smaller/150, arrowEnd=True)
    
    minuteAngle = minute * 360 / (60)
    angleRadians = math.radians(minuteAngle)
    dx =  0.65 * r * math.sin(angleRadians)
    dy =  0.65 * r * math.cos(angleRadians)
    drawLine(cx, cy, cx+dx, cy-dy, fill="black", lineWidth=smaller/200, arrowEnd=True)
    
    

def drawClockFace(app):
    cx = app.width/2
    cy = app.height/2
    smaller = min(app.width, app.height)

    drawCircle(cx, cy, smaller/60)

    r = 0.9 * (smaller/2)
    drawCircle(cx, cy, r, fill=None, border="black")
    
    numRadius = r * 0.85
    
    # Draw the tic marks for minutes
    for i in range(60):
        minuteAngle = i * 360 / (60)
        angleRadians = math.radians(minuteAngle)
        endX =  cx + r * math.sin(angleRadians)
        endY =  cy - r * math.cos(angleRadians)
        startX =  cx + 0.975 * r * math.sin(angleRadians)
        startY =  cy - 0.975 * r * math.cos(angleRadians)
        drawLine(startX, startY, endX, endY, lineWidth=smaller/600)
    
    # Draw the tic marks for hours
    for i in range(0, 12):
        hourAngle = i * 360 / 12
        angleRadians = math.radians(hourAngle)
        endX =  cx + r * math.sin(angleRadians)
        endY =  cy - r * math.cos(angleRadians)
        startX =  cx + 0.95 * r * math.sin(angleRadians)
        startY =  cy - 0.95 * r * math.cos(angleRadians)
        drawLine(startX, startY, endX, endY, lineWidth=smaller/300)
    
    # Draw the numbers
    for i in range(1, 13):
        angle = (360/12)*i
        angleRadians = math.radians(angle)
        dx = numRadius * math.sin(angleRadians)
        dy = numRadius * math.cos(angleRadians)
        #drawCircle(cx+dx, cy-dy, 5)
        drawLabel(str(i), cx+dx, cy-dy, size=smaller//20)

def onStep(app):
    app.step += 1
    if app.step % (45 * 60) == 0:
        app.min += 1
        if app.min == 60:
            app.min = 0
            app.hour += 1
        if app.hour == 13:
            app.hour = 1

def onAppStart(app):
    app.step = 0
    app.hour = 2
    app.min = 35

def redrawAll(app):
    drawClockFace(app)
    drawClockHands(app, app.hour, app.min)

runApp(width=800, height=600)
