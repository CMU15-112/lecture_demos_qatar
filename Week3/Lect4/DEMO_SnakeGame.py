from cmu_graphics import *
import math
import random


def reset(app):
    app.snake=[(0,0)]
    app.direction= (0, +1)
    app.status= "welcome"
    placeFood(app)

    
# Controller Function: called ONCE when the app starts
def onAppStart(app):    
    app.rows= 10
    app.cols= 10
    app.sideL= app.width//app.cols
    reset(app)

    
def placeFood(app):
    
    while True:
        r = random.randint(0, app.rows-1)
        c = random.randint(0, app.cols-1)
        
        if (r,c) not in app.snake:
            app.foodPosition= (r, c)
            return
        
    
# Controller Function: called presses with the mouse on the canvas
def onMousePress(app, x, y):
    pass
       
def takeStep(app):
    r, c= app.snake[0]
    newR= r + app.direction[0]
    newC= c + app.direction[1]
    
    if newR < 0 or newR >= app.rows or newC < 0 or newC >= app.cols or (newR, newC) in app.snake:
        app.status = "gameOver"
    else: 
        app.snake.insert(0, (newR, newC)) # newCell
        
        if (newR, newC) == app.foodPosition:
            placeFood(app)
        else: 
            app.snake.pop()
    
    
    
    
# Controller Function: called when user pressed a key
def onKeyPress(app, key):
    if app.status == "welcome":
        app.status = "playing"
        
    print(f"key: {key}")
    if key == "up":
        app.direction= (-1, 0)
        takeStep(app)
    elif key == "down":
        app.direction= (+1, 0)
        takeStep(app)
    elif key == "right":
        app.direction = (0, +1)
        takeStep(app)
    elif key == "left":
        app.direction = (0, -1)
        takeStep(app)
    elif key in "Rr":
        reset(app)
        app.status= "playing"

    
    
    #
    
    
#Controller Function: called by default 30 times per second
def onStep(app):
    pass

def drawBoard(app):
    for r in range(app.rows):
        for c in range(app.cols):
            drawRect(c*app.sideL, r*app.sideL, app.sideL, app.sideL, fill= None, border="black")
    
def cellCenterCoords(app, r, c):
    cx= c*app.sideL + app.sideL//2
    cy= r*app.sideL + app.sideL//2
    
    return cx, cy

def drawSnake(app):
    
    radius= app.sideL//4
    
    first= True
    for r,c in app.snake:
        if first:
            color= "red"
            first= False
        else:
            color= "blue"
        cx, cy=  cellCenterCoords(app, r, c)
        drawCircle(cx, cy, radius, fill= color)
        
  
def drawFood(app):
    
    radius= app.sideL//4
    
    cx, cy=  cellCenterCoords(app, app.foodPosition[0], app.foodPosition[1])
    drawCircle(cx, cy, radius, fill= "green")
        
    
# This is the view - called after every controller function
def redrawAll(app):
    if app.status == "welcome":
        drawLabel("Press Any Key to start the Game", app.width//2, app.height//2, size= 30, bold=True)
    elif app.status == "playing":
        drawBoard(app)
        drawSnake(app)
        drawFood(app)
    else: # gameOver
        drawLabel("Game Over !!! Press (r) to restart", app.width//2, app.height//2, size= 30, bold=True)

        
    #pass


runApp(width=800, height=800)