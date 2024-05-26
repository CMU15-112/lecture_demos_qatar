from cmu_graphics import *
import math
import random

def reset(app):
    print("onAppStart")
    app.stepsPerSecond=10 # updates per second
    app.cnt = 0
    app.x = app.width//2
    app.y= app.height//2
    app.r= 150
    app.points= 0
    app.speed= 5 # pixels per update
    app.dx= 0 # -1
    app.dy= -1
    app.gameOver= False
    
# This is called when the program starts
def onAppStart(app):
    reset(app)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
    
def moveTarget(app):
    #Option 1) Moving to a random location (called inside onMousePress)
    #app.x=random.randint(app.r, app.width-app.r)
    #app.y=random.randint(app.r, app.height-app.r)
    
    #Option 2) Keep moving over time (called inside onStep)
    app.x= app.x+ (app.speed * app.dx)
    app.y= app.y+ (app.speed * app.dy)
    
    if app.x + app.r >= app.width or app.x - app.r <=0 :
        app.dx *= -1
        
    if app.y+ app.r >= app.height or app.y - app.r <= 0:     
        app.dy *= -1
    

    
def onMousePress(app, x, y):
    # x,y coords of where mouse pressed
    print(f"onMousePress ({x}, {y})")
    
    #if user clicked inside the target
    if distance(app.x, app.y, x, y) < app.r//5:
        app.points+=1
        app.r-=50
        
        if app.r <= 0:
            app.r = 1
            app.gameOver= True
    
        #Option 1) moveTarget(app): moves target to a random location when the user clicks the center of the target

def onKeyPress(app, key):
    # x,y coords of where mouse pressed
    print(f"onKeyPress ({key})")
    
    if key in "rR":
        reset(app)
    
# This is called many times to refresh the window
def redrawAll(app):
    #print("redrawAll")
    drawLabel(f"{app.points} in {app.cnt/app.stepsPerSecond} secs ", app.width//2, app.height//30, size= app.height//20)
    
    if app.gameOver:
        drawLabel("Game Over- You Won !! ", app.width//2, app.height//2, size= app.height//20)

    else:
        r= app.r
        c= 0
        for i in range(5):
            
            if c%2==0:
                color='red'
            else:
                color = 'white'
                
            drawCircle(app.x, app.y, r, fill=color)
            r-= (app.r/5)
            c+=1
    
def onStep(app):
    #print(f" onStep {app.stepsPerSecond}")
    if app.gameOver == False:
        app.cnt+=1    
        moveTarget(app)

    
# This is how you run the programS
runApp(width=800, height=800)

