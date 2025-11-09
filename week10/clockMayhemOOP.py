from cmu_graphics import *
import math
import random

class Clock:
    # this is a class variable (it's shared across all instances)
    randomColors = ['blue', 'yellow', 'red', 'green', 'pink']
    def __init__(self, app, radius):
        dirs = [-1, 1]
        self.cx = random.randint(radius, app.width -  radius)
        self.cy = random.randint(radius, app.height -  radius)
        self.dx = dirs[random.randint(0,1)]
        self.dy = dirs[random.randint(0,1)]
        self.radius = radius
        self.color = Clock.randomColor()
        
    # this is a class method (note it doesn't get self)
    # it's normally used for functions that do not depend on
    # one particular instance
    def randomColor():
        return Clock.randomColors[random.randint(0,len(Clock.randomColors)-1)]
    
    def randomizeColor(self):
        self.color = Clock.randomColor()
    # updates the clock position according to the current speed
    # retrieves the canvas dimensions and speed from the model
    def updateClockPos(self, app):
        self.cx += app.speed * self.dx
        if self.cx + self.radius > app.width:
            self.cx = app.width - self.radius
            self.dx  *= -1
        elif self.cx <= self.radius:
            self.cx = self.radius
            self.dx  *= -1

        # vertical movement
        self.cy  += app.speed * self.dy
        if self.cy >= (app.height - self.radius):
             self.cy = app.height - self.radius
             self.dy *= -1
        elif self.cy <= self.radius:
             self.cy = self.radius
             self.dy *= -1
             
    def pointInsideClock(self, app, x, y):
        return ((self.cx - x)**2 + (self.cy - y)**2) <= self.radius**2

    # mm: integer, minutes, 0-59
    # ss: integer, seconds, 0-59
    # cx, cy, radius: center coordinates and clock radius
    def drawHands(self, app):
        radius = self.radius
        hh = app.hh
        mm = app.mm
        ss = app.ss
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

        drawLine(self.cx, self.cy, \
                 self.cx + hRadius * math.cos(math.radians(hAngle)), \
                 self.cy + hRadius * math.sin(math.radians(hAngle)), \
                 arrowEnd = True, lineWidth = hWidth)
        drawLine(self.cx, self.cy, \
                 self.cx + mRadius * math.cos(math.radians(mAngle)), \
                 self.cy + mRadius * math.sin(math.radians(mAngle)), \
                 arrowEnd = True, lineWidth = mWidth)
        drawLine(self.cx, self.cy, \
                 self.cx + sRadius * math.cos(math.radians(sAngle)), \
                 self.cy + sRadius * math.sin(math.radians(sAngle)), \
                 arrowEnd = False, lineWidth = sWidth)

    # assumes a clock with a given radius centered at (cx, cy)
    def drawNumbers(self, app):
        smallRadius = 0.85*self.radius
        num = 3
        fontSize = self.radius//8
        # approach: start from 3  -> 3 corresponds to angle 0 with inverted axes
        for angle in range(0, 360, 30):
            angle = math.radians(angle)
            hourX = self.cx + smallRadius * math.cos(angle)
            hourY = self.cy + smallRadius * math.sin(angle)
            label = str(num)
            drawLabel(label, hourX, hourY,bold=True,size=fontSize)
            num = num%12 + 1


    # draws a clock with bounding box width x height
    def drawClockFace(self, app):
        drawCircle(self.cx, self.cy, self.radius, fill=self.color)
        
    # the main draw function for a clock
    def draw(self, app):
        self.drawClockFace(app)
        self.drawNumbers(app)
        self.drawHands(app)
        

def restart(app):
  
    app.state = 'welcome'
    app.counter = 0
    
    app.speed = 10 # pixels per move
    


    app.clocks = []
    for i in range(5):
        app.clocks.append(Clock(app, app.clockRadius))

  

def onAppStart(app):
    app.hh = 11
    app.mm = 41
    app.ss = 26
 
    app.clockRadius = min(app.width, app.height)//10
  
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
            clock.updateClockPos(app)  # clock moves
    if app.counter % 60 == 0:
        for clock in app.clocks:
            clock.randomizeColor()


def onMousePress(app, x, y):
    
    for i in range(len(app.clocks)):
        clock = app.clocks[i]
        if clock.pointInsideClock(app, x, y) \
           and clock.color == 'green':
            # clock i should removed
            app.clocks.pop(i)
            return  # return as soon as I see a green clock
    # if i get here, i never detected a click on a green clock 
    app.speed *= 1.1
            
    

# hh: integer, hours 1 - 12

def redrawAll(app):
    clockRad = app.clockRadius
    fontSize = app.height//15
    if app.state == 'welcome':
        drawLabel("Welcome to Clock Mayhem",
                  app.width//2, app.height//2-2*fontSize,
                  size=fontSize)
        drawLabel("Catch the green wall clocks",
                  app.width//2, app.height//2+2*fontSize,
                  size=fontSize)
        drawLabel("Press 's' to start",
                  app.width//2, app.height//2+4*fontSize,
                  size=fontSize)
        
        
        
    elif app.state == 'play':
        for clock in app.clocks:
            clock.draw(app)
            
runApp(600, 600)

