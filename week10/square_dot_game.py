from cmu_112_graphics import *
import random

# This sets up the model
def appStarted(app):
    # Configuration
    app.timerDelay = 16
    app.speed = 10
    app.blips = 0
    
    # The rectangle
    app.cx = app.width/2
    app.cy = app.height/2
    app.rWidth = 75
    app.rHeight = 25
    
    # The dots
    # Convention: (x,y,r,color)
    app.dots = []

def timerFired(app):
    app.blips += 1
    if app.blips % 10 == 0:
        x = random.randint(0,app.width)
        y = random.randint(0,app.height)
        r = random.randint(5,10)
        dx = random.choice([-1,1])
        dy = random.choice([-1,1])
        color = random.choice(["red","yellow","blue","green"])
        app.dots.append( [x,y,r,color,dx,dy] )
        
    for dot in app.dots:
        dot[0] += dot[4]
        dot[1] += dot[5]
        

# This is part of the controller
def keyPressed(app, event):
    if event.key == "Left":
        app.cx -= app.speed
    elif event.key == "Right":
        app.cx += app.speed
    elif event.key == "Up":
        app.cy -= app.speed
    elif event.key == "Down":
        app.cy += app.speed

# This is the view
def redrawAll(app, canvas):    
    for x,y,r,color,dx,dy in app.dots:
        canvas.create_oval(x-r,y-r,x+r,y+r,fill=color)
        
    x1 = app.cx-app.rWidth/2
    y1 = app.cy-app.rHeight/2
    x2 = app.cx+app.rWidth/2
    y2 = app.cy+app.rHeight/2
    canvas.create_rectangle(x1,y1,x2,y2,fill="red")

runApp(width=800, height=800)