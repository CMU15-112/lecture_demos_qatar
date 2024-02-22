from cmu_graphics import *

def drawBoard(app):
    sideL = app.width // app.numCols
    
    for r in range(app.numRows):
        for c in range(app.numCols):
            x = c * sideL
            y = r * sideL
            
            drawRect(x, y, sideL, sideL, border="black", fill="blue")
            drawCircle(x + sideL/2, y + sideL/2, sideL/3, fill=app.board[r][c])

def onAppStart(app):
    app.numRows = 6
    app.numCols = 7

    app.board = []
    for i in range(app.numRows):
        app.board.append(["white"] * app.numCols)
        
    app.player = "red"
    app.invalidCol = False

def onMousePress(app, x, y):
    col = x // (app.width // app.numCols)
    
    for r in range(app.numRows-1, -1, -1):
        if app.board[r][col] == "white":
            app.invalidCol = False
            app.board[r][col] = app.player
            if app.player == "red":
                app.player = "yellow"
            else:
                app.player = "red"
            return
    # No spots available
    app.invalidCol = True
    
def redrawAll(app):
    drawBoard(app)
    drawLabel(f"{app.player}'s turn", app.width/2, app.height-80, size=40)
    
    if app.invalidCol:
        drawLabel("Invalid column, try again", app.width/2, app.height-40, size=40)
    
runApp(800,800)