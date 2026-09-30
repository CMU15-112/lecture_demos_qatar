from cmu_graphics import *
import math
import random

def randomizeTarget(app, t):
    t[0] = random.randint(t[2], app.width - t[2])
    t[1] = random.randint(t[2], app.height - t[2])

def onAppStart(app):
    app.counter = 0
    app.points = 0
    app.gameOver = False
    app.targets = []
    app.targets.append([app.width//2, app.height//2, 40])

def onStep(app):
    app.counter += 1
    
    if app.counter % 60 == 0:
        for t in app.targets:
            randomizeTarget(app, t)

def onMousePress(app, x, y):
    for t in app.targets[:]:
        d = math.sqrt((x - t[0]) ** 2 + (y - t[1]) ** 2)
        if d < t[2]:
            t[2] = max(1, t[2] - 5)
            if t[2] > 1:
                # Successful click on target
                print(app.counter, 60 / (app.counter % 60 + 1))
                app.points += 1 + 60 / (app.counter % 60 + 1)
                randomizeTarget(app, t)
                app.counter = 0
                
                # Add another target
                newTarget = [app.width//2, app.height//2, 40]
                app.targets.append(newTarget)
            elif t[2] <= 1:
                app.gameOver = True            

def drawTarget(app, t):
    x, y, r = t
    for i in range(5):
        if i%2 == 0:
            color = 'red'
        else:
            color = 'white'
        tempR = r - (i * r / 5)
        drawCircle(x, y, tempR,fill=color)    

def redrawAll(app):
    if app.gameOver:
        drawLabel("Game Over", app.width//2, app.height//2, size=30)
    else:
        for t in app.targets:
            drawTarget(app, t)
    drawLabel(f"{app.points:.2f} points", app.width // 2, 20, size=20)

runApp(width=800, height=800)
