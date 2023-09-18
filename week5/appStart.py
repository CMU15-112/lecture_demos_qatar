from cmu_graphics import *
import random

def onAppStart(app):
    app.counter = 0
    app.countDown = 5 # seconds
    app.steps = 0
    app.dotColor = "red"
    app.dotR = random.randint( 20, 50)  # choose a random radius
    app.dotX = random.randint(app.dotR, app.width - app.dotR)  # choose a random starting loc
    app.dotY = random.randint(app.dotR, app.height - app.dotR)
    app.gameState = "play"

    #app.stepsPerSecond = 10
    print("Hello from appStart")

def onMousePress(app, x, y):
    print(f"Hello from onMousePress {x} {y}")

def onKeyPress(app, key):
    print(f"Hello from onKeyPress {key}")
    app.count += 1
    print(f"so far {app.count} key presses")


def onStep(app):
    app.steps += 1
    if app.steps % 30 == 0:
        app.countDown -=1
    if app.countDown <= 0:
        app.gameState = "game over"


def redrawAll(app):
    if app.gameState == "game over":
        drawRect(0,0,app.width, app.height, fill="red")
        drawLabel("Game Over", app.width//2, app.height//2, fill="white", size=60) 
    if app.gameState == "play":  
        drawLabel(f'{app.counter} clicks on the target', app.width//2, 100, size=60 )

        drawLabel(f"Time Remaining: {app.countDown}", app.width, app.height, 
                align='right-bottom', size=60)
        drawCircle(app.dotX, app.dotY, app.dotR, fill=app.dotColor)


runApp(800, 800)