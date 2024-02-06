from cmu_graphics import *

# This is called when the program starts
def onAppStart(app):
    app.circleX = 0
    app.circleY = 0
    app.cnt = 0

# This is called every time one key is pressed
def onKeyPress(app, key):
    pass

# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    app.circleX = x
    app.circleY = y

# This is called many times to refresh the window
def redrawAll(app):
    drawCircle(app.circleX, app.circleY, 20)
    drawLabel(f"{app.cnt/30:.2f}",app.width//2, app.height//2, size = app.height//20)

# This is called "often" (def. by app.stepsPerSecond)
def onStep(app):
    app.cnt += 1

# This is how you run the program
runApp(width=800, height=800)

