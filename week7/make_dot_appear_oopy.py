from cmu_112_graphics import *
# every mouse pressed, draw a green dot, 20 px radius, at the position of
# the mouse pressed
import random

class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = random.randint(5, 20)
        self.color = random.choice(["red","yellow","blue","green"])
        self.dx = -1
        self.dy  = -1
        
    def draw(self, app, canvas):
        canvas.create_oval(self.x-self.r,self.y-self.r,
                           self.x+self.r,self.y+self.r,
                           fill=self.color)

def appStarted(app):
    app.counter = 0
    app.dots = []
    app.r = 20
    app.timerDelay = 100
    app.gameState = "play"
    


def mousePressed(app, event):
    for i in range(len(app.dots)):
        d = ((event.x - app.dots[i].x)**2 + (event.y-app.dots[i].y)**2)**0.5
        if d <= app.dots[i].r:
            # Usually shouldn't remove from a list you are looping through,
            # but we return immediately after, so the bug won't manifest
            app.dots.pop(i)
            break
    if len(app.dots) == 0:
        print("Win")
        app.gameState = "win"
        
def timerFired(app):
    
    for dot in app.dots:
        dot.x += dot.dx
        dot.y += dot.dy
        
    if app.counter%100==0:
        x= random.randint(0, app.width)
        y= random.randint(0, app.height)
        newdot = Dot(x, y)
        app.dots.append(newdot)
    app.counter += 1
    

    
def redrawAll(app, canvas):
    if app.gameState == "play":
        for dot in app.dots:
            dot.draw(app, canvas)
    elif app.gameState == "win":
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        
        
 
  
runApp(width=800, height=600)