from cmu_graphics import *

def drawConnectFour(app):
    # Find the smallest cell size based on width and height
    cellWidth = app.cellWidth
    boardWidth = cellWidth * app.numCols
    boardHeight = cellWidth * app.numRows
    
    drawRect(0,0, boardWidth, boardHeight, fill="blue")
    
    for r in range(len(app.board)):
        for c in range(len(app.board[r])):
            color = app.board[r][c]
            x = c * cellWidth
            y = r * cellWidth
            drawCircle(x+cellWidth/2, y+cellWidth/2, cellWidth * .45, fill=color)
            #drawCircle(x, y, cellWidth * .45, fill=color, align="top-left")

def findEmptySlot(app, c):
    for r in range(len(app.board)-1, -1, -1):
        if app.board[r][c] == "white":
            return r
    return None

def containsFourInRow(tokenList):
    for i in range(len(tokenList)):
        subSlice = tokenList[i:i+4]
        if subSlice[0] != "white" and subSlice.count(subSlice[0]) == 4:
            return subSlice[0]
    return None

def isGameOver(app):
    for row in app.board:
        winner = containsFourInRow(row)
        if winner:
            return winner
    return None

def reset(app):
    app.numCols = 7
    app.numRows = 6
    app.cellWidth = min(app.width/app.numCols, app.height/app.numRows)

    app.player = 0
    app.colors = ["red", "yellow"]

    
    app.board = []
    for r in range(app.numRows):
        app.board.append(["white"] * app.numCols)
        
    app.gameOver = False

# Controller
def onAppStart(app):
    reset(app)

# Controller
def onMousePress(app, x, y):
    if app.gameOver:
        return
    
    if x  <= app.cellWidth * app.numCols and y <= app.cellWidth * app.numRows:
        c = int(x // app.cellWidth)
        r = findEmptySlot(app, c)
        if r != None:
            app.board[r][c] = app.colors[app.player]
            app.player = (app.player + 1) % 2
            winner = isGameOver(app)
            if winner:
                print("Winner!", winner)
                app.gameOver = True
                app.winner = winner

# Controller
def onKeyPress(app, key):
    pass
 
# View
def redrawAll(app):
    drawConnectFour(app)
    w = app.cellWidth * app.numCols
    h = app.cellWidth * app.numRows
    if app.gameOver:
        drawRect(0,0,w,h,fill="grey",opacity=65)
        drawLabel(f"{app.winner} is the winner!", w/2, h/2, size=app.cellWidth/2, fill="white")

# Controller
def onStep(app):
    # I feel dirty
    app.cellWidth = min(app.width/app.numCols, app.height/app.numRows)

runApp(width=800, height=800)