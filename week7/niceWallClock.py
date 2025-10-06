from cmu_graphics import *
import math
import random

def onAppStart(app):
    app.hh = 11
    app.mm = 41
    app.ss = 26
    app.clockColor = 'yellow'
    app.counter = 0
    app.cx, app.cy = app.width//2, app.height//2
    app.clockRadius = min(app.width, app.height)//10
    app.dx = 1  # (-1: right to left, 1: left to right)
    app.speed = 10 # pixels per move
    app.dy = 1  #

    dirs = [-1, 1]
    app.clocks = []
    for i in range(5):
        # clockInfo: cx, cy, dx, dy
        cx = random.randint(app.clockRadius, app.width -  app.clockRadius)
        cy = random.randint(app.clockRadius, app.height -  app.clockRadius)
        dx = dirs[random.randint(0,1)]
        dy = dirs[random.randint(0,1)]
        app.clocks.append([cx,cy,dx,dy])


    #app.stepsPerSecond = 30


# advances the clock by one second.
# handles rollover of seconds -> minutes -> hours,
# keeping time in hh:mm:ss format with hours wrapped modulo 12.
def oneMoreSecond(app):
    app.ss += 1
    if app.ss % 60 == 0:
        app.mm += 1
        if app.mm % 60 == 0:
            app.hh += 1
    app.ss = app.ss % 60
    app.mm = app.mm % 60
    app.hh = app.hh % 12

# this is a CONTROLLER helper
def updateClockPos(app, clock):
    # we stopped here
    pass

def onStep(app):
    app.counter += 1
    print(f'{app.counter}. Hey there')
    if app.counter % 30 == 0:
        oneMoreSecond(app)  # once every 30 calls
    if app.counter % 2 == 0:  # once every 2 calls
        for clock in app.clocks:
            updateClockPos(app, clock)



# hh: integer, hours 1 - 12
# mm: integer, minutes, 0-59
# ss: integer, seconds, 0-59
# cx, cy, radius: center coordinates and clock radius
def drawHands(cx, cy, radius, hh, mm, ss ):
    # this formulas give the angle (in degrees) based on time
    hAngle = (((hh - 3)% 12) + mm/60) * (360/12)  # 3:00 -> 0deg
    mAngle = ((mm - 15)% 60) * (360/60) # 15min -> 0deg
    sAngle = ((ss - 15)% 60) * (360/60) # 15seg -> 0deg

    # Hand lengths
    hRadius = 0.4 * radius #(70% of clock face)
    mRadius = 0.6 * radius #(70% of clock face)
    sRadius = 0.7 * radius #(70% of clock face)

    #Hand widths
    hWidth = 0.05 * radius
    mWidth = 0.03 * radius
    sWidth = 0.01 * radius

    drawLine(cx, cy, \
             cx + hRadius * math.cos(math.radians(hAngle)), \
             cy + hRadius * math.sin(math.radians(hAngle)), \
             arrowEnd = True, lineWidth = hWidth)
    drawLine(cx, cy, \
             cx + mRadius * math.cos(math.radians(mAngle)), \
             cy + mRadius * math.sin(math.radians(mAngle)), \
             arrowEnd = True, lineWidth = mWidth)
    drawLine(cx, cy, \
             cx + sRadius * math.cos(math.radians(sAngle)), \
             cy + sRadius * math.sin(math.radians(sAngle)), \
             arrowEnd = False, lineWidth = sWidth)

# assumes a clock with a given radius centered at (cx, cy)
def drawNumbers(cx, cy, radius):
    smallRadius = 0.85*radius
    num = 3
    fontSize = radius//8
    # approach: start from 3  -> 3 corresponds to angle 0 with inverted axes
    for angle in range(0, 360, 30):
        angle = math.radians(angle)
        hourX = cx + smallRadius * math.cos(angle)
        hourY = cy + smallRadius * math.sin(angle)
        label = str(num)
        drawLabel(label, hourX, hourY,bold=True,size=fontSize)
        num = num%12 + 1


# draws a clock with bounding box width x height
def drawClockFace(cx, cy, radius, color = 'yellow'):
    drawCircle(cx, cy, radius, fill=color)

def redrawAll(app):
    clockRad = app.clockRadius

    for clock in app.clocks:

        drawClockFace(clock[0], clock[1],
                      clockRad, 'yellow' )
        drawNumbers(clock[0], clock[1], clockRad)
        drawHands(clock[0], clock[1],
                  clockRad,
                  app.hh, app.mm, app.ss)

runApp(600, 600)
runApp(600, 600)
runApp(600, 600)
runApp(600, 600)
