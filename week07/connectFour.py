from cmu_graphics import *

# Check to see if the current player has won
def checkWinner(app):
    winSequence = app.curPlayer * 4
    
    # Check Horizontal
    for r in range(app.numRows):
        testRow = "".join(app.board[r])
        if winSequence in testRow:
            return True
        
    # Check Vertical
    for c in range(app.numCols):
        testCol = ""
        for r in range(app.numRows):
            testCol += app.board[r][c]
        if winSequence in testCol:
            return True
        
    # Check Diagonals
    for r in range(3, app.numRows):
        tempR = r
        tempC = 0
        test = ""
        while tempR < app.numRows and tempC < app.numCols:
            test += app.board[tempR][tempC]
            tempR -= 1
            tempC += 1
        if winSequence in test:
            return True
        
    
    return False

def drawBoard(app):
    for r in range(app.numRows):
        for c in range(app.numCols):
            x = c * app.sideL + app.offsetX
            y = r * app.sideL + app.offsetY
            drawRect(x, y, app.sideL, app.sideL, fill="lightblue", border="black", borderWidth=1)
            
            cx = x + app.sideL/2
            cy = y + app.sideL/2
            
            drawCircle(cx, cy, app.sideL/2 * 0.8, fill=app.board[r][c])

# This is called when the program starts
def onAppStart(app):
    app.numRows = 6
    app.numCols = 7
    
    guess1 = app.width // app.numCols
    guess2 = app.height // app.numRows

    if guess1 > guess2:
        app.sideL = guess2
        app.offsetX = (app.width - (app.sideL * app.numCols))//2
        app.offsetY = 0
    else:
        app.sideL = guess1
        app.offsetX = 0
        app.offsetY = (app.height - (app.sideL * app.numRows))//2

    app.curPlayer = "Red"
    
    app.gameOver = False

    app.board = []
    for r in range(app.numRows):
        app.board.append(["White"] * app.numCols)
            
    #app.board = [["White"]*app.numCols for i in range(app.numRows)]
    
# This is called every time one key is pressed
def onKeyPress(app, key):
    pass

# This is called every time a mouse button is pressed
def onMousePress(app, x, y):
    colNum = (x - app.offsetX) // app.sideL
    if colNum < 0 or colNum > app.numCols - 1:
        return
    
    # Find the first empty slot in column colNum
    r = app.numRows - 1
    while app.board[r][colNum] != "White" and r >= 0:
        r -= 1
    
    if r >= 0:
        app.board[r][colNum] = app.curPlayer
        if checkWinner(app):
            app.gameOver = True
            return
        
        if app.curPlayer == "Red":
            app.curPlayer = "Yellow"
        else:
            app.curPlayer = "Red"
    
    print(colNum)
    pass

# This is called many times to refresh the window
def redrawAll(app):
    if app.gameOver:
        drawLabel(f"Game Over: {app.curPlayer} won", app.width//2, app.height//2)
    else:
        drawBoard(app)

# This is called "often" (def. by app.stepsPerSecond)
def onStep(app):
    pass

# This is how you run the program
runApp(width=1200, height=800)