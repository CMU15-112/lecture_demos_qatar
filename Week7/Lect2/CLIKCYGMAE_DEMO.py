from cmu_graphics import *
import math
import random

# Controller Function: called ONCE when the app starts
def onAppStart(app):
    app.state= "welcome"
    app.rows= 5
    app.cols= 5
    app.sideL = app.width//app.cols #assuming width and height are equal
    app.countDown= 10
    app.stepsPerSecond= 1
    
    
    ## randomly assign colors to grid cells
    colors = ['red', 'blue', 'green']
    
    app.cellColors = [] #2D (stores list of colors for each row)
    for r in range(app.rows): #5
        cl = [] # stores colors for current row
        for c in range(app.cols): # 5
            indx = random.randint(0,2)
            cl.append(colors[indx])
        # list of colors for the current row
        app.cellColors.append(cl)
    
    
def allCellsSameColor(app):
    
    seenColor = None
    
    for r in app.cellColors: # list of colors
        for c in r: # one color
            if c != 'white':
                if seenColor == None:
                    seenColor = c
                elif seenColor != c:
                    return False
        
    return True
            
    
    
# Controller Function: called presses with the mouse on the canvas
def onMousePress(app, x, y):
    if app.state == 'playing':
        c = x //app.sideL
        r = y //app.sideL
        app.cellColors[r][c] = 'white'
            
        if allCellsSameColor(app):
            app.state = 'win'
            
# Controller Function: called when user pressed a key
def onKeyPress(app, key):
    if key in "sS":
        app.state= "playing"
    
#Controller Function: called by default 30 times per second
def onStep(app):
    if app.state == 'playing':
        app.countDown -= 1
        if app.countDown == 0:
            app.state = 'gameOver'
    

def drawGrid(app):
    for r in range(app.rows):
        for c in range(app.cols):
            drawRect(c*app.sideL, r*app.sideL, app.sideL, app.sideL,
                     fill=app.cellColors[r][c]) #change fill color
    
# This is the view - called after every controller function
def redrawAll(app):
    
    if app.state=="welcome":
        welcomeText = """Welcome to ClickyGame
    Click on the colored cells to remove them
    You win when all remaining
    colored cells have the same color
    You have 10 seconds
    Press s to start"""
        drawRect(0,0, app.width, app.height, fill="green")
        y= app.height//3
        for l in welcomeText.split("\n"):
            drawLabel(l, app.width//2, y, size= 30, fill="white")        
            y+= 30
            
    elif app.state=="playing": #playing
        drawGrid(app)
        drawLabel(f"Time Remaining: {app.countDown}", app.width//2, 20, size= 30, fill="black")        

    elif app.state== "win":
        drawRect(0,0, app.width, app.height, fill="blue")
        drawLabel("You WON !!!", app.width//2, app.height//2, size= 50, fill="white")
        
    else: 
        drawRect(0,0, app.width, app.height, fill="blue")
        drawLabel("Game OVER !!!", app.width//2, app.height//2, size= 50, fill="white")        

        

runApp(width=600, height=600)