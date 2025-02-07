from cmu_graphics import *
import math

def onAppStart(app):
    app.counter = 1
    app.ss = 0  # seconds
    app.mm = 45 # minutes
    app.hh = 3  # hours
    app.stepsPerSecond = 30  #default value

    app.dx = 1  # movement direction on the x-axis
    app.dy = 1  # movement direciton on the y-axis
    app.sx = 2  # speed in x
    app.sy = 2  # speed in y

    app.cx = app.width//2  # center  x
    app.cy = app.height//2 # center y
    app.clockRadiusPer = 0.25 # 1/4 of min(app.width, app.height)

    app.state ='welcome'  # states = {welcome, go, paused}
    app.clockColor = 'yellow'  # initial color

# this function updates the current time
# advances seconds by one
def oneMoreSecond(app):
    app.ss += 1
    if app.ss % 60 == 0:
        app.mm += 1
        if app.mm % 60 == 0:
            app.hh += 1
    app.ss = app.ss % 60
    app.mm = app.mm % 60
    app.hh = app.hh % 12

# checks if the point (x,y) is inside the clock (circle)
def pointInsideClock(app, x, y):
    clockRad = int(min(app.width, app.height) * app.clockRadiusPer)
    return (x-app.cx)**2 + (app.cy-y)**2 <= clockRad**2

# switches the color yellow <-> pink
# updates the model accordingly
def changeClockColor(app):
    if app.clockColor == 'yellow':
        app.clockColor = 'pink'
    else:
        app.clockColor = 'yellow'

# just use a formula to get the radius based on the current window width
def getClockRadius(app):
    return int(min(app.width, app.height) * app.clockRadiusPer)

# capture mouse press
def onMousePress(app, x, y):
    print(f'DEBUG: mouse @{x},{y}')
    if pointInsideClock(app, x, y):
        print("DEBUG: click inside")
        changeClockColor(app)


# Updates the clock position using the current direction and speed
# Checks colission with the window border to "bounce"
def updateClockPos(app):
    clockRad = getClockRadius(app)
    # update x coordinate
    app.cx += (app.dx * app.sx)
    # (horizontal) bounce back if needed
    # bounce from the right side
    if app.cx >= (app.width - clockRad):
        app.cx = app.width - clockRad
        app.dx *= -1
    # or bounce from the left size
    elif app.cx <= clockRad:
        app.cx = clockRad
        app.dx *= -1
    # updata y coordinate
    app.cy += (app.dy * app.sy)
    # (vertical) bounce back if needed
    # bounce from the bottom
    if app.cy >= (app.height - clockRad):
        app.cy = app.height - clockRad
        app.dy *= -1
    # or the top
    elif app.cy <= clockRad:
        app.cy = clockRad
        app.dy *= -1

# increase speed by 2 px per step
def increaseSpeed(app):
    app.sx += 2
    app.sy += 2
    # let's set a max speed (don't go too fast)
    # 50 pixels per step is quite fast
    app.sx = min(50, app.sx)
    app.sy = min(50, app.sy)
def decreaseSpeed(app):
    app.sx -= 2
    app.sy -= 2
    # we don't want the speed to become negative
    app.sx = max(0, app.sx)
    app.sy = max(0, app.sy)

def onKeyPress(app, key):
    print(f'DEBUG: pressed {key}')

    # some keys only work for a specific anim state
    if app.state == 'welcome':
        if key == 's':
            app.state = 'go'
    elif app.state == 'go':
        if key == 'p':
            app.state = 'paused'
        elif key == '+':
            increaseSpeed(app)
        elif key == '-':
            decreaseSpeed(app)
    elif app.state == 'paused':
        if key == 'g':
            app.state = 'go'

    # some keys work in multiple states
    if app.state == 'go' or app.state == 'paused':
        if key == 'n':
            oneMoreSecond(app)



def onStep(app):
    if app.state == 'go':
        app.counter += 1
        if app.counter % app.stepsPerSecond == 0:
            oneMoreSecond(app)
        updateClockPos(app)

# hh: integer, hours 1 - 12
# mm: integer, minutes, 0-59
# ss: integer, seconds, 0-59
# cx, cy, radius: center coordinates and clock radius
def drawHands(app):
    clockRad = getClockRadius(app)
    # this formulas give the angle (in degrees) based on time
    hAngle = ((app.hh - 3)% 12) * (360/12)  # 3:00 -> 0deg
    mAngle = ((app.mm - 15)% 60) * (360/60) # 15min -> 0deg
    sAngle = ((app.ss - 15)% 60) * (360/60) # 15seg -> 0deg

    # Hand lengths
    hRadius = 0.4 * clockRad #(40% of clock face)
    mRadius = 0.6 * clockRad #(60% of clock face)
    sRadius = 0.7 * clockRad #(70% of clock face)

    #Hand widths
    hWidth = 0.08 * clockRad
    mWidth = 0.05 * clockRad
    sWidth = 0.02 * clockRad

    drawLine(app.cx, app.cy, \
             app.cx + hRadius * math.cos(math.radians(hAngle)), \
             app.cy + hRadius * math.sin(math.radians(hAngle)), \
             arrowEnd = True, lineWidth = hWidth)
    drawLine(app.cx, app.cy, \
             app.cx + mRadius * math.cos(math.radians(mAngle)), \
             app.cy + mRadius * math.sin(math.radians(mAngle)), \
             arrowEnd = True, lineWidth = mWidth)
    drawLine(app.cx, app.cy, \
             app.cx + sRadius * math.cos(math.radians(sAngle)), \
             app.cy + sRadius * math.sin(math.radians(sAngle)), \
             arrowEnd = False, lineWidth = sWidth)

def drawNumbers(app):
    clockRad = getClockRadius(app)
    smallRadius = 0.85*clockRad
    num = 3
    fontSize = clockRad*0.25  # 25% of the clock face
    # approach: start from 3  -> 3 corresponds to angle 0 with inverted axes
    for angle in range(0, 360, 30):
        angle = math.radians(angle)
        hourX = app.cx + smallRadius * math.cos(angle)
        hourY = app.cy + smallRadius * math.sin(angle)
        label = str(num)
        drawLabel(label, hourX, hourY,bold=True,size=fontSize)
        num = num%12 + 1


def drawClockFace(app):
    clockRad = getClockRadius(app)
    drawCircle(app.cx,app.cy,clockRad, fill=app.clockColor)

def redrawAll(app):
    if app.state == 'welcome':
        fontSize = min(app.width, app.height)*0.05  # 5% of the 'shortest' window length
        drawLabel("Welcome to the Crazy Clock Example",
                  app.width//2, app.height//2 - fontSize*2) # shift toward the top
        drawLabel("Press 's' to start",
                  app.width//2, app.height//2)
    else:
        drawClockFace(app)
        drawNumbers(app)
        drawHands(app)
        if app.state == 'paused':
            fontSize = getClockRadius(app)*0.25  # 25% of the clock face
            drawLabel("Freeze!", app.cx, app.cy, fill='red', size=fontSize)
            drawLabel("Press g to resume", app.cx, app.cy+fontSize, fill='red', size=fontSize)


runApp(600, 600)
