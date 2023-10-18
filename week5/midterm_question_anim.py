from cmu_graphics import *
import random

def restart(app):
    app.cx = app.width//2
    app.cy = app.height//2
    app.r = app.height//10
    app.gameOver = False
    app.pressedRect = False
    app.nSteps = 0


def onAppStart(app):
    app.stepsPerSecond = 4
    restart(app)
def redrawAll(app):
    if app.gameOver:
        drawLabel("game Over", app.width//2, app.height//2)
    else:
        drawCircle(app.cx, app.cy, app.r, fill="blue")
        drawRect(app.width//2, app.height//2, 20, 20, align='center')

def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def onMousePress(app, x, y):
    if app.width//2 - 10 <= x <= app.width//2 + 10 \
    and app.height//2 - 10 <= y <= app.height//2 + 10:
        app.pressedRect = True
    else:
            if dist(app.cx, app.cy, x, y) < app.r and app.pressedRect == True:
                app.r //= 2
                app.cx = random.randint(app.r, app.width-app.r)
                app.cy = random.randint(app.r, app.height-app.r)
            app.pressedRect=False
def onKeyPress(app, key):
    if key == 'r':
        restart(app)
def gameOver(app):
    if app.cx + app.r >= app.width or app.cx - app.r < 0:
        return True
    if app.cy + app.r >= app.height or app.cy - app.r < 0:
        return True

    return False
def onStep(app):
    app.nSteps += 1
    if app.nSteps % 15 == 0:
            app.r += 1
    if gameOver(app):
        app.gameOver = True
runApp(600, 300)

