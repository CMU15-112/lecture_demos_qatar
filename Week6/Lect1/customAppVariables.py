from cmu_graphics import *

# This is called when the program starts
def onAppStart(app):
    print("onAppStart")
    app.stepsPerSecond=10


# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    # x,y coords of where mouse pressed
    print(f"onMousePress ({x}, {y})")



# This is called every time one key is pressed
def onKeyPress(app, key):
    # x,y coords of where mouse pressed
    print(f"onKeyPress ({key})")
    
    
    
# This is called many times to refresh the window
def redrawAll(app):
    print("redrawAll")
    
    

# This is called "often" (def. by app.stepsPerSecond)    
def onStep(app):
    print(f" onStep {app.stepsPerSecond}")

    
    
# This is how you run the programS
runApp(width=800, height=800)