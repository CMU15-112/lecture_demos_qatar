from cmu_graphics import *
import random

def moveTarget(app):
    app.cx = random.randint(app.maxRadius, app.width-app.maxRadius)
    app.cy = random.randint(app.maxRadius, app.height-app.maxRadius)

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def reset(app):
    app.stepCount = 0
    app.gameOver = False
    app.points = 0
    app.minRadius = 10
    app.maxRadius = 20
    app.radius = (app.maxRadius-app.minRadius)//2 + app.minRadius
    app.radiusDir = 1
    app.cx = app.width//2
    app.cy = app.height//2
    moveTarget(app)

def onAppStart(app):
    reset(app)
      
def onMousePress(app, x, y):
    if app.gameOver == False:
        if distance(app.cx, app.cy, x, y) <= app.radius:
            app.points += 1
            moveTarget(app)
            app.maxRadius -= 5
            app.minRadius -= 5
        
def onKeyPress(app, key):
    if app.gameOver == True and key == 'r':
        reset(app)

def onStep(app):
    if app.gameOver == False:
        app.stepCount += 1
        if app.radius >= app.maxRadius:
            app.radiusDir = -1
        elif app.radius <= app.minRadius:
            app.radiusDir = 1

        app.radius += app.radiusDir
        if app.minRadius <= 0:
            app.gameOver = True

def redrawAll(app):
    
    if app.gameOver:
        drawLabel("Game Over!", app.width//2, app.height//2, size=50)
        drawLabel("Press (r) to reset", app.width//2, app.height//2 + app.height//5, size=30)
    else:
        for i in range(5):
            if i%2 == 0:
                color = 'red'
            else:
                color = 'white'
            r = app.radius - (i * app.radius / 5)
            drawCircle(app.cx, app.cy, r,fill=color)
    
    drawLabel(f"Points: {app.points}, Time: {app.stepCount/30:.2f}", app.width/2, 50, size=40)

runApp(width=800, height=800)