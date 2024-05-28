from cmu_graphics import *
import math
import random

# Controller Function: called ONCE when the app starts
def onAppStart(app):
    app.state= "welcome"
    app.rows= 5
    app.cols= 5
    app.countDown= 10
    app.stepsPerSecond= 1
    
    colors= ["red", "green", "blue"]
    app.cellColors=[]
    for r in range(app.rows):
        row= []
        for c in range(app.cols):
            row.append(colors[random.randint(0,2)])
        app.cellColors.append(row)
    
    
def allCellsSameColor(app):
    
    colorSeen= None
    for r in range(app.rows):
        for c in range(app.cols):
            color= app.cellColors[r][c]
            
            if color != "white":
                if colorSeen== None:
                    colorSeen= color
                elif colorSeen != color:
                    return False
    return True
                
    
# Controller Function: called presses with the mouse on the canvas
def onMousePress(app, x, y):
    cellW= app.width//app.cols
    cellH= app.height//app.rows
    c= x//cellW
    r= y//cellH    
    app.cellColors[r][c]= "white"
    if allCellsSameColor(app):
        app.state= "win"
        print("WON")
            
# Controller Function: called when user pressed a key
def onKeyPress(app, key):
    if key in "sS":
        app.state= "playing"
    
#Controller Function: called by default 30 times per second
def onStep(app):
    if app.state == "playing":
        if app.countDown ==0:
            print("GAME OVER")
            app.state= "losing"
        else:
            app.countDown-= 1
    

def drawGrid(app):
    h= app.height//app.rows
    w= app.width//app.cols
    for r in range(app.rows):
        for c in range(app.cols):
            drawRect(c*w, r*h, w, h, fill=app.cellColors[r][c])
    
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
        
        y= app.height//2
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

        

runApp(width=800, height=800)