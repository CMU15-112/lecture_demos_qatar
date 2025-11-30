from cmu_graphics import *
import math
import random
from clock import Clock


# The server is hosted here:
# https://github.com/CMU-15112Q/clockmayhem-multiplayer-server
# and it's deployed on the cloud using render (free account)
GAMESERVERURL = "clock-mayhem-multiplayer-server.onrender.com"

class DrawableClock(Clock):
    def __init__(self, cid, cx, cy, color, radius=50, canvasSize=600):
        super().__init__(cid, radius=radius, canvasSize=canvasSize)
        self.cx = cx
        self.cy = cy
        self.color = color

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
    app.clocks = []


#------- This is the multi-player part --------
import websockets
import asyncio
import threading
import json

def loadClock(d):
    cid = d['id']
    cx = d['cx']
    cy = d['cy']
    color = d['color']
    return DrawableClock(cid, cx, cy, color)

async def updateClocks(app, data):
    app.clocks = []
    if 'clocks' in data:
        for c in data['clocks']:
            app.clocks.append(loadClock(c))

async def receiveUpdates(app):
    async with websockets.connect(f'wss://{GAMESERVERURL}/ws') as websocket:
        while True:
            rawdata = await websocket.recv()
            data = json.loads(rawdata)
            await updateClocks(app, data)

def runAsyncInThread(coro):
    def runner():
        asyncio.run(coro)
    t = threading.Thread(target=runner)
    t.start()
    return t
# ------------------------------------------


def onAppStart(app):
    app.hh = 11
    app.mm = 41
    app.ss = 26

    app.clockRadius = min(app.width, app.height)//10

    restart(app)
    runAsyncInThread(receiveUpdates(app))

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
    # nothing now, it's all done in the server
    pass


def onMousePress(app, x, y):
    for i in range(len(app.clocks)):
        clock = app.clocks[i]
        if clock.pointInsideClock(x, y) \
           and clock.color == 'green':
            # clock i should removed
            app.clocks.pop(i)
            return  # return as soon as I see a green clock



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
