from cmu_graphics import *

# This is called when the program starts
def onAppStart(app):
    print("onAppStart")
    app.stepsPerSecond=10
    app.cnt = 0
    app.x = app.width//2
    app.y= app.height//2

def onMousePress(app, x, y):
    # x,y coords of where mouse pressed
    print(f"onMousePress ({x}, {y})")
    app.x= x
    app.y= y
    #drawCircle(app.x, app.y, 20, fill='red') # MVC ERROR

def onKeyPress(app, key):
    # x,y coords of where mouse pressed
    print(f"onKeyPress ({key})")
    
# This is called many times to refresh the window
def redrawAll(app):
    print("redrawAll")
    drawLabel(f"{app.cnt/app.stepsPerSecond} secs ", app.width//2, app.height//2, size= app.height//20)
    drawCircle(app.x, app.y, 20, fill='red')
    
def onStep(app):
    #print(f" onStep {app.stepsPerSecond}")
    app.cnt+=1
    
# This is how you run the programS
runApp(width=800, height=800)
