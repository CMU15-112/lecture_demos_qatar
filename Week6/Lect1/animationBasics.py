from cmu_graphics import *

    
# This is called when the program starts
def onAppStart(app):
    print("onAppStart")
    app.stepsPerSecond=10
    app.steps = 0
    app.cx = app.width//2
    app.cy = app.height//2


# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    # x,y coords of where mouse pressed
    print(f"onMousePress ({x}, {y})")
    app.cx = x
    app.cy = y



# This is called every time one key is pressed
def onKeyPress(app, key):
    # x,y coords of where mouse pressed
    print(f"onKeyPress ({key})")
    
    
# This is called many times to refresh the window
def redrawAll(app):
    print("redrawAll")
    drawLabel(f"{app.steps/app.stepsPerSecond}", app.width//2, app.height//2, size = 50 )
    drawCircle(app.cx, app.cy, 50, fill="red")


# This is called "often" (def. by app.stepsPerSecond)    
def onStep(app):
    print(f" onStep {app.stepsPerSecond}")
    app.steps+=1
    
    
    
# This is how you run the programS
runApp(width=800, height=800)