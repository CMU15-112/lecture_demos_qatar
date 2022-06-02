from cmu_112_graphics import *
# every mouse pressed, random color, random radius, at the position of
# the mouse pressed
import random

class Dot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = random.randint(5, 20)
        self.color = random.choice(["red","yellow","blue","green"])
    def draw(self, canvas):
        canvas.create_oval(self.x-self.r,self.y-self.r,
                           self.x+self.r,self.y+self.r,
                           fill=self.color)
    def changeColor(self):
        self.color = random.choice(["red","yellow","blue","green"])
        
    

def appStarted(app):
    app.dots = []
    app.counter = 0
    

#controller
def timerFired(app):
    app.counter += 1
    if app.counter % 40 == 0:
        for dot in app.dots:
            dot.changeColor()
    
    

def mousePressed(app, event):
    newdot = Dot(event.x, event.y)
    app.dots.append(newdot)

    
def redrawAll(app, canvas):
    for dot in app.dots:
        dot.draw(canvas)

  
runApp(width=800, height=600)