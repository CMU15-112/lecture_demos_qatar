from cmu_graphics import *
import math
import random


def reset(app):
    app.status= "welcome"
    app.points= 0
    app.cnt = 0
    app.snake = [(0, 0)]
    app.direction = (0, +1)
    placeFood(app)
    
    
# Controller Function: called ONCE when the app starts
def onAppStart(app):    
    app.rows= 10
    app.cols= 10
    app.sideL= app.width//app.cols
    reset(app)

    
def placeFood(app):

    fr = random.randint(0,app.rows-1)
    fc = random.randint(0, app.cols-1)
    
    while (fr, fc) in app.snake:
        fr = random.randint(0,app.rows-1)
        fc = random.randint(0, app.cols-1)
     
    app.foodPosition= (fr, fc)

def takeStep(app):
    hr, hc = app.snake[0]
    newR = hr + app.direction[0]
    newC = hc + app.direction[1]
    
    if newC < 0 or newC >= app.cols or newR <0 or newR >= app.rows or (newR, newC) in app.snake:
        app.status = "gameOver"
    else:    
        app.snake.insert(0, (newR, newC))
        
        if (newR, newC) == app.foodPosition:
            placeFood(app)
            app.points+=1
        else:   
            app.snake.pop()
    
    
    
# Controller Function: called when user pressed a key
def onKeyPress(app, key):
    if app.status == "welcome":
        app.status = "playing"
        
    print(f"key: {key}")
    if key in "Rr":
        reset(app)
        app.status= "playing"
    elif key == "up":
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


def drawBoard(app):
    for r in range(app.rows):
        for c in range(app.cols):
            drawRect(c*app.sideL, r*app.sideL, app.sideL, app.sideL, fill= None, border="black")
    
# find coordinates given rowID and colID
def cellCenterCoords(app, r, c):
    cx= c*app.sideL + app.sideL//2
    cy= r*app.sideL + app.sideL//2
    
    return cx, cy

def drawSnake(app):
    
    first = True
    for r,c in app.snake:
     
        
        if first:
            fc = 'red'
        else:
            fc = 'blue'
            
        first = False
        cx, cy = cellCenterCoords(app, r, c)
        drawCircle(cx, cy, app.sideL//4, fill=fc)
        
  
def drawFood(app):
    cx, cy = cellCenterCoords(app, app.foodPosition[0], app.foodPosition[1])
    drawStar(cx, cy, app.sideL//4, 5, fill='orange')
        
#Controller Function: called by default 30 times per second
def onStep(app):
    if app.status == "playing":
        app.cnt += 1
    
# This is the view - called after every controller function
def redrawAll(app):
    
    drawLabel(f"{app.points} Points in {rounded(app.cnt/app.stepsPerSecond)} secs ", app.width//2, app.height//30, size= app.height//20)

    if app.status == "welcome":
        drawLabel("Press Any Key to start the Game", app.width//2, app.height//2, size= 30, bold=True)

    elif app.status == "playing":
        drawBoard(app)
        drawSnake(app)
        drawFood(app)

    else: # gameOver
        drawLabel("Game Over !!! Press (r) to restart", app.width//2, app.height//2, size= 30, bold=True)

        
    #pass


runApp(width=600, height=600)
