from cmu_graphics import *
import random

class Dot(object):
    def __init__(self, x, y, r, dx, dy, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy

    def draw(self, app):
        drawCircle(self.x, self.y, self.r, fill=self.color)

    def move(self, app):

        if self.x + self.r > app.width or self.x - self.r < 0:
            self.dx *= -1
        if self.y + self.r > app.height or self.y - self.r < 0:
            self.dy *= -1
        self.x += self.dx
        self.y += self.dy
    def isClicked(self, x, y):
        d = ((x-self.x)**2 + (y-self.y)**2)**0.5
        return d <= self.r




# This sets up the model
def onAppStart(app):
    # Configuration
    app.speed = 10 # px per step
    app.blips = 0

    # The rectangle [x, y, width, height]
    app.player = [app.width//2, app.height//2, 75, 25]


    # The dots
    app.dots = []

def createRandomDot(app, x, y):
    r = random.randint(20,40)
    dx = random.choice([-1,0,1])
    dy = random.choice([-1,0,1])
    color = random.choice(["red","blue","green"])
    app.dots.append( Dot(x,y,r,dx,dy,color) )

def onStep(app):
    app.blips += 1

    # every 5 seconds, one new dot appear
    if app.blips % (5 * app.stepsPerSecond) == 0:
        r = random.randint(20,40)
        x = random.randint(r,app.width-r)
        y = random.randint(r,app.height-r)
        dx = random.choice([-1,0,1])
        dy = random.choice([-1,0,1])
        color = random.choice(["red","blue","green"])
        app.dots.append( Dot(x,y,r,dx,dy,color) )

    # dots move
    for dot in app.dots[:]:
        dot.move(app)

        circleXDist = abs(dot.x - app.player[0])
        circleYDist = abs(dot.y - app.player[1])
       

        if circleXDist < app.player[2]/2 + dot.r and \
           circleYDist < app.player[3]/2 + dot.r:
            app.dots.remove(dot)

def onMousePress(app, x, y):
    for dot in app.dots[:]:
        if dot.isClicked(x, y):
            # Usually shouldn't remove from a list you are looping through,
            # but we return immediately after, so the bug won't manifest
            app.dots.remove(dot)
            return
    createRandomDot(app,x,y)

# This is part of the controller
def onKeyPress(app, key):
    print(key)
    if key == "left":
        app.player[0] -= app.speed
    elif key == "right":
        app.player[0] += app.speed
    elif key == "up":
        app.player[1] -= app.speed
    elif key == "down":
        app.player[1] += app.speed
    elif key in "fF":
        app.player[2], app.player[3] = app.player[3], app.player[2]

# This is the view
def redrawAll(app):
    for dot in app.dots:
        dot.draw(app)
        #drawCircle(dotX, dotY, r, fill=color)
    drawRect(app.player[0], app.player[1],
        app.player[2], app.player[3],fill="red")


runApp(width=800, height=800)
