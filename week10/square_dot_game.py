from cmu_112_graphics import *
import random

class Dot(object):
    def __init__(self, x, y, r, color, dx, dy):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        
    def draw(self, app, canvas):
        canvas.create_oval(self.x-self.r,self.y-self.r,
                           self.x+self.r,self.y+self.r,
                           fill=self.color)
        
class Rect(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        
    def draw(self, app, canvas):
        x1 = self.x-self.w/2
        y1 = self.y-self.h/2
        x2 = self.x+self.w/2
        y2 = self.y+self.h/2
        canvas.create_rectangle(x1,y1,x2,y2,fill="red")

# This sets up the model
def appStarted(app):
    # Configuration
    app.timerDelay = 33
    app.speed = 10
    app.blips = 0
    
    # The rectangle
    app.player = Rect(app.width/2, app.height/2, 75, 25)
    
    # The dots
    # Convention: (x,y,r,color)
    app.dots = []

def timerFired(app):
    app.blips += 1
    
    if app.blips % (1000//app.timerDelay) == 0:
        r = random.randint(5,10)
        x = random.randint(r,app.width-r)
        y = random.randint(r,app.height-r)
        dx = random.choice([-1,1])
        dy = random.choice([-1,1])
        color = random.choice(["red","yellow","blue","green"])
        app.dots.append( Dot(x,y,r,color,dx,dy) )
        
    for dot in app.dots[:]:
        dot.x += dot.dx
        dot.y += dot.dy
        
        if dot.x+dot.r > app.width or dot.x-dot.r < 0:
            dot.dx *= -1
        if dot.y+dot.r > app.height or dot.y-dot.r < 0:
            dot.dy *= -1
    
        circleXDist = abs(dot.x - app.player.x)
        circleYDist = abs(dot.y - app.player.y)
        
        if circleXDist < app.player.w/2 + dot.r and \
           circleYDist < app.player.h/2 + dot.r:
            app.dots.remove(dot)

def mousePressed(app, event):
    for dot in app.dots:
        d = ((event.x-dot.x)**2 + (event.y-dot.y)**2)**0.5
        if d <= dot.r:
            # Usually shouldn't remove from a list you are looping through,
            # but we return immediately after, so the bug won't manifest
            app.dots.remove(dot)
            return

# This is part of the controller
def keyPressed(app, event):
    if event.key == "Left":
        app.player.x -= app.speed
    elif event.key == "Right":
        app.player.x += app.speed
    elif event.key == "Up":
        app.player.y -= app.speed
    elif event.key == "Down":
        app.player.y += app.speed
    elif event.key in "fF":
        (app.player.w,app.player.h) = (app.player.h, app.player.w)

# This is the view
def redrawAll(app, canvas):    
    for dot in app.dots:
        dot.draw(app, canvas)
        
    app.player.draw(app, canvas)

runApp(width=800, height=800)