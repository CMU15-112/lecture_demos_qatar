from cmu_graphics import *
import math
import random

def onAppStart(app):
    app.colors = ['red', 'green', 'blue']
    app.grid = ""
    app.nrows = 5
    app.ncols = 5
    app.countDown = 10  # countdown timer in seconds
    app.counter = 0
    app.stepsPerSecond = 20 # 50 milliseconds
    app.cellColors = []
    for row in range(app.nrows):
        rowColors = []
        for col in range(app.ncols):
            random.shuffle(app.colors)
            randomColor = app.colors[0]
            rowColors.append(randomColor)  # choose a random color
        app.cellColors.append(rowColors)
    app.gameState = 'welcome'
            
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
    
def onMousePress(app, x, y):
    if app.gameState == 'playing':
        selected = selectedCell(app, x, y)
        if selected != None:  # selected piece
            cellCol = selected[0]
            cellRow = selected[1]
            print(f"selected {cellCol}, {cellRow}")
            app.cellColors[cellRow][cellCol] = 'white'
        if allCellsSameColor(app):
            app.gameState = 'win'
            
def onKeyPress(app, key):
    if app.gameState == 'welcome':
        if key == 's':
            app.gameState = 'playing'
    
def onStep(app):
    app.counter += 1
    if app.gameState == 'playing':
        if app.counter % 20 == 0:  # every 20 counter increments (1 second)
            app.countDown -= 1
            if app.countDown == 0:  # game over
                app.gameState = "gameOver"

def drawGrid(width, height, cellColors, nrows, ncols):
    cellSize = (width)//ncols, (height)//nrows  
    for row in range(nrows):
        for col in range(ncols):
            # compute coordinates
            x1 = cellSize[0] * col
            y1 = cellSize[1] * row
            # find the corresponding color
            curColor = cellColors[row][col]
            # draw the rectangle
            drawRect(x1, y1, cellSize[0], cellSize[1], fill=curColor)

# This is the view
def redrawAll(app):
    if app.gameState == "gameOver":
        drawRect(0,0,app.width, app.height, fill="blue")
        drawLabel("Game Over", app.width//2, app.height//2, fill="white", \
            font="Arial", size=60, bold=True)
    elif app.gameState == "welcome":
        drawRect(0,0,app.width, app.height, fill="green")
        welcomeText = """Welcome to ClickyGame
Click on the colored cells to remove them
You win when all remaining
colored cells have the same color
You have 10 seconds
Press s to start"""
        offset = 0
        for line in welcomeText.split('\n'):
            drawLabel(line, app.width//2, offset+app.height//2, \
                fill="white", font="Arial", size = 20, bold=True)
            offset += 25

    elif app.gameState == "win":
        drawRect(0,0,app.width, app.height, fill="blue")
        drawLabel("You Won", app.width//2, app.height//2, fill="white", \
            font="Arial", size=60, bold=True)
    else:
        fontSize = min(app.width, app.height)//5
        drawGrid(app.width, app.height, app.cellColors, app.nrows, app.ncols, )
        drawLabel(f"Time Remaining: {app.countDown}", app.width, app.height, \
            font="Arial", size=fontSize//7, bold=True, align='left-bottom')


runApp(width=800, height=800)