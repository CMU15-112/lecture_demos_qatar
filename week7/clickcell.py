from cmu_112_graphics import *
import math
import random

def appStarted(app):
    app.colors = ['red', 'green', 'blue']
    app.grid = ""
    app.nrows = 5
    app.ncols = 5
    app.countDown = 10  # countdown timer in seconds
    app.counter = 0
    app.timerDelay = 50 # milliseconds
    app.cellColors = []
    for row in range(app.nrows):
        rowColors = []
        for col in range(app.ncols):
            random.shuffle(app.colors)
            randomColor = app.colors[0]
            rowColors.append(randomColor)  # choose a random color
        app.cellColors.append(rowColors)
    app.gameState = 'playing'
            
def selectedCell(app, x, y):
    # It is basically the same code that draws, but without drawing
    cellSize = (app.width)//app.ncols, (app.height)//app.nrows  
    for row in range(app.nrows):
        for col in range(app.ncols):
            # compute coordinates
            x1 = cellSize[0] * col
            y1 = cellSize[1] * row
            x2 = x1 + cellSize[0]
            y2 = y1 + cellSize[1]
            if x1 <= x <= x2 and y1 <= y <= y2:
                return col, row
    return None  # no cell selected

# helper function to check if all non-white cells
# are colored the same
def allCellsSameColor(app):
    nred, ngreen, nblue = 0, 0, 0
    for row in range(app.nrows):
        for col in range(app.ncols):
            if app.cellColors[row][col] == 'red':
                nred += 1
            if app.cellColors[row][col] == 'green':
                ngreen += 1
            if app.cellColors[row][col] == 'blue':
                nblue += 1
    return (nred == 0 and ngreen == 0) or \
       (nred == 0 and nblue ==0) or \
       (ngreen == 0 and nblue ==0 )
        
def mousePressed(app, event):
    if app.gameState == 'playing':
        selected = selectedCell(app, event.x, event.y)
        if selected != None:  # selected piece
            cellCol = selected[0]
            cellRow = selected[1]
            print(f"selected {cellCol}, {cellRow}")
            app.cellColors[cellRow][cellCol] = 'white'
        if allCellsSameColor(app):
            app.gameState = 'win'
            

def timerFired(app):
    app.counter += 1 
    if app.counter % 20 == 0:  # every 20 counter increments (1 second)
        app.countDown -= 1
        if app.countDown == 0:  # game over
            app.gameState = "gameOver"

def drawGrid(canvas, width, height, cellColors, nrows, ncols):
    cellSize = (width)//ncols, (height)//nrows  
    for row in range(nrows):
        for col in range(ncols):
            # compute coordinates
            x1 = cellSize[0] * col
            y1 = cellSize[1] * row
            x2 = x1 + cellSize[0]
            y2 = y1 + cellSize[1]
            # find the corresponding color
            curColor = cellColors[row][col]
            # draw the rectangle
            canvas.create_rectangle(x1, y1, x2, y2,
                                    fill=curColor)

# This is the view
def redrawAll(app, canvas):
    if app.gameState == "gameOver":
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        canvas.create_text(app.width//2, app.height//2, text="Game Over", fill="white", font="Arial 60 bold")
    elif app.gameState == "win":
        canvas.create_rectangle(0,0,app.width, app.height, fill="blue")
        canvas.create_text(app.width//2, app.height//2, text="You Won", fill="white", font="Arial 60 bold")
    else:
        fontSize = min(app.width, app.height)//5
        drawGrid(canvas, app.width, app.height, app.cellColors, app.nrows, app.ncols, )
        canvas.create_text(app.width, app.height, text=f"Time Remaining: {app.countDown}",
                           font=f"Arial {fontSize//7} bold", anchor='se')


runApp(width=1400, height=1400)