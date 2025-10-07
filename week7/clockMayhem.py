from cmu_graphics import *
import math
import random

def restart(app):
  
    app.state = 'welcome'
    app.counter = 0
    
    app.speed = 10 # pixels per move
    

    dirs = [-1, 1]
    app.clocks = []
    for i in range(5):
        # clockInfo: cx, cy, dx, dy, color
        cx = random.randint(app.clockRadius, app.width -  app.clockRadius)
        cy = random.randint(app.clockRadius, app.height -  app.clockRadius)
        dx = dirs[random.randint(0,1)]
        dy = dirs[random.randint(0,1)]
        color = randomColor(app)
        app.clocks.append([cx,cy,dx,dy, color])


def randomColor(app):
    return app.randomColors[random.randint(0,len(app.randomColors)-1)]
    

def onAppStart(app):
    app.hh = 11
    app.mm = 41
    app.ss = 26
 
    app.clockRadius = min(app.width, app.height)//10
  
    app.randomColors = ['blue', 'yellow', 'red', 'green', 'pink']
    restart(app)

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
    cx, cy = clock[0], clock[1]
    dx, dy = clock[2], clock[3]
    
    cx += app.speed * dx
    if cx + app.clockRadius > app.width:
        cx = app.width - app.clockRadius
        dx  *= -1
    elif cx <= app.clockRadius:
        cx = app.clockRadius
        dx  *= -1

    # vertical movement
    cy  += app.speed * dy
    if cy >= (app.height - app.clockRadius):
         cy = app.height - app.clockRadius
         dy *= -1
    elif cy <= app.clockRadius:
         cy = app.clockRadius
         dy *= -1
         
    clock[0], clock[1] = cx, cy
    clock[2], clock[3] = dx, dy

def onKeyPress(app, key):
    if app.state == 'welcome':
        if key == 's':
            app.state = 'play'
    if key == 'r':
        restart(app)
def onStep(app):
    app.counter += 1
    #print(f'{app.counter}. Hey there')
    if app.counter % 30 == 0:
        oneMoreSecond(app)  # once every 30 calls
    if app.counter % 2 == 0:  # once every 2 calls
        for clock in app.clocks:
            updateClockPos(app, clock)  # clock moves
    if app.counter % 60 == 0:
        for clock in app.clocks:
            clock[4] = randomColor(app)

def pointInsideClock(app, cx, cy, x, y):
    return ((cx - x)**2 + (cy - y)**2) <= app.clockRadius**2

def onMousePress(app, x, y):
    
    for i in range(len(app.clocks)):
        clock = app.clocks[i]
        cx, cy = clock[0], clock[1]
        if pointInsideClock(app, cx, cy, x, y) \
           and clock[4] == 'green':
            # clock i should removed
            app.clocks.pop(i)
            return  # return as soon as I see a green clock
    # if i get here, i never detected a click on a green clock 
    app.speed *= 1.1
            
    

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
    fontSize = app.height//15
    if app.state == 'welcome':
        drawLabel("Welcome to Clock Mayhem",
                  app.width//2, app.height//2-2*fontSize,
                  size=fontSize)
        drawLabel("Press 's' to start",
                  app.width//2, app.height//2+2*fontSize,
                  size=fontSize)
        
    elif app.state == 'play':

        for clock in app.clocks:

            drawClockFace(clock[0], clock[1],
                          clockRad, clock[4] )
            drawNumbers(clock[0], clock[1], clockRad)
            drawHands(clock[0], clock[1],
                      clockRad,
                      app.hh, app.mm, app.ss)

runApp(600, 600)

