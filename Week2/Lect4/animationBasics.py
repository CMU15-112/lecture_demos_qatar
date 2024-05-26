from cmu_graphics import *

# This is called when the program starts
def onAppStart(app):
    print("onAppStart")
    app.stepsPerSecond=1

def onMousePress(app, x, y):
    # x,y coords of where mouse pressed
    print(f"onMousePress ({x}, {y})")

def onKeyPress(app, key):
    # x,y coords of where mouse pressed
    print(f"onKeyPress ({key})")
    
# This is called many times to refresh the window
def redrawAll(app):
    print("redrawAll")
    
def onStep(app):
    print(f" onStep {app.stepsPerSecond}")

    
# This is how you run the programS
runApp(width=800, height=800)