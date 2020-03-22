from cmu_112_graphics import *
import random

# model (app)
def appStarted(app):
    # the number of milliseconds between calls to timerFired
    app.timerDelay = 20
    
    app.squareX = app.width//2
    app.squareY = app.height//2
    app.squareSize = 20
    app.dx = 1
    app.dy = 1
    
    app.circles = []

# controller
def timerFired(app):
    app.squareX += app.dx
    app.squareY += app.dy
    
    if (app.squareY+app.squareSize//2) >= app.height:
        app.dy *= -1
    elif (app.squareX+app.squareSize//2) >= app.width:
        app.dx *= -1
    elif (app.squareY-app.squareSize//2) <= 0:
        app.dy *= -1
    elif (app.squareX-app.squareSize//2) <= 0:
        app.dx *= -1
    
    circleX = random.randint(0,app.width)
    circleY = random.randint(0,app.height)
    circleR = 20
    
    app.circles.append( (circleX, circleY, circleR) )

# controller
def keyPressed(app, event):
    if event.key == "Left":
        app.squareX -= 5
    elif event.key == "Right":
        app.squareX += 5
    elif event.key == "Up":
        app.squareY -= 5
    elif event.key == "Down":
        app.squareY += 5

# view
def redrawAll(app, canvas):
    for c in app.circles:
        canvas.create_oval(c[0]-c[2]//2,
                            c[1]-c[2]//2,
                            c[0]+c[2]//2,
                            c[1]+c[2]//2,
                            fill="orange")
        
    canvas.create_rectangle(app.squareX-app.squareSize//2,
                            app.squareY-app.squareSize//2,
                            app.squareX+app.squareSize//2,
                            app.squareY+app.squareSize//2,
                            fill="blue") 
    

runApp(width=800, height=400)