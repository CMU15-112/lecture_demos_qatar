from cmu_112_graphics import *
import random

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 5 # margin around grid
    app.timerDelay = 250
    initSnakeAndFood(app)
    app.waitingForFirstKeyPress = True

def initSnakeAndFood(app):
    app.snake = [(0,0)]
    app.direction = (0, +1) # (drow, dcol)
    placeFood(app)
    app.gameOver = False

# getCellBounds from grid-demo.py
def getCellBounds(app, row, col):
    # aka 'modelToView'
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col+1) / app.cols
    y0 = app.margin + gridHeight * row / app.rows
    y1 = app.margin + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def keyPressed(app, event):
    if (app.waitingForFirstKeyPress):
        app.waitingForFirstKeyPress = False
    elif (event.key == 'r'):
        initSnakeAndFood(app)
    elif app.gameOver:
        return
    elif (event.key == 'Up'):      app.direction = (-1, 0)
    elif (event.key == 'Down'):  app.direction = (+1, 0)
    elif (event.key == 'Left'):  app.direction = (0, -1)
    elif (event.key == 'Right'): app.direction = (0, +1)
    # elif (event.key == 's'):
        # this was only here for debugging, before we turned on the timer
        # takeStep(app)
def mousePressed(app, event):
    print(event.x, event.y)
def timerFired(app):
    if app.gameOver or app.waitingForFirstKeyPress: return
    takeStep(app)

def takeStep(app):
    (drow, dcol) = app.direction
    (headRow, headCol) = app.snake[0]
    (newRow, newCol) = (headRow+drow, headCol+dcol)
    if ((newRow < 0) or (newRow >= app.rows) or
        (newCol < 0) or (newCol >= app.cols) or
        ((newRow, newCol) in app.snake)):
        app.gameOver = True
    else:
        app.snake.insert(0, (newRow, newCol))
        if (app.foodPosition == (newRow, newCol)):
            placeFood(app)
        else:
            # didn't eat, so remove old tail (slither forward)
            app.snake.pop()

def placeFood(app):
    # Keep trying random positions until we find one that is not in
    # the snake. Note: there are more sophisticated ways to do this.
    while True:
        row = random.randint(0, app.rows-1)
        col = random.randint(0, app.cols-1)
        if (row,col) not in app.snake:
            app.foodPosition = (row, col)
            return

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill='white')

def drawSnake(app, canvas):
    for (row, col) in app.snake:
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill='blue')

def drawFood(app, canvas):
    if (app.foodPosition != None):
        (row, col) = app.foodPosition
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill='green')

def drawGameOver(app, canvas):
    if (app.gameOver):
        canvas.create_text(app.width/2, app.height/2, text='Game over!',
                           font='Arial 26 bold')
        canvas.create_text(app.width/2, app.height/2+40,
                           text='Press r to restart!',
                           font='Arial 26 bold')

def redrawAll(app, canvas):
    if (app.waitingForFirstKeyPress):
        canvas.create_text(app.width/2, app.height/2,
                           text='Press any key to start!',
                           font='Arial 26 bold')
    else:
        drawBoard(app, canvas)
        drawSnake(app, canvas)
        drawFood(app, canvas)
        drawGameOver(app, canvas)

runApp(width=400, height=400)