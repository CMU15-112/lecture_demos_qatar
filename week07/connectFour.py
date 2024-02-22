from cmu_graphics import *

def isSubList(L1, L2):
    for i in range(len(L2)):
        subList = L2[i:i+len(L1)]
        if L1 == subList:
            return True
    return False

def getCol(app, c):
    # Return a list containing all of the colors from column c
    ret = []
    for r in range(app.numRows):
        ret.append(app.board[r][c])
    return ret

def getDiagDownFrom(app, r, c):
    ret = []
    while r < app.numRows and c < app.numCols:
        ret.append(app.board[r][c])
        r += 1
        c += 1
    return ret

def getDiagUpFrom(app, r, c):
    ret = []
    while r < app.numRows and c < app.numCols:
        ret.append(app.board[r][c])
        r += -1
        c += 1
    return ret

# Return the winner if there is a winner, or None otherwise
def isWinner(app):
    # Check horizontal rows
    for r in range(app.numRows):
        if isSubList(["red"]*4, app.board[r]):
            return "red"
        elif isSubList(["yellow"]*4, app.board[r]):
            return "yellow"
    
    # Check vertical cols
    for c in range(app.numCols):
        tmp = getCol(app, c)
        if isSubList(["red"]*4, tmp):
            return "red"
        elif isSubList(["yellow"]*4, tmp):
            return "yellow"

    # Check diag from along the left
    for r in range(app.numRows):
        tmp = getDiagDownFrom(app, r, 0)
        if isSubList(["red"]*4, tmp):
            return "red"
        elif isSubList(["yellow"]*4, tmp):
            return "yellow"
    
    # Check diag from along the top
    for c in range(app.numCols):
        tmp = getDiagDownFrom(app, 0, c)
        if isSubList(["red"]*4, tmp):
            return "red"
        elif isSubList(["yellow"]*4, tmp):
            return "yellow"
        
    # Check diag from along the left
    for r in range(app.numRows):
        tmp = getDiagUpFrom(app, r, 0)
        if isSubList(["red"]*4, tmp):
            return "red"
        elif isSubList(["yellow"]*4, tmp):
            return "yellow"
    
    # Check diag from along the bottom
    for c in range(app.numCols):
        tmp = getDiagUpFrom(app, app.numRows-1, c)
        if isSubList(["red"]*4, tmp):
            return "red"
        elif isSubList(["yellow"]*4, tmp):
            return "yellow"
    return None

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
    
    app.gameOver = False
    app.winner = None

def onMousePress(app, x, y):
    if app.gameOver:
        return
    
    col = x // (app.width // app.numCols)
    
    for r in range(app.numRows-1, -1, -1):
        if app.board[r][col] == "white":
            app.invalidCol = False
            app.board[r][col] = app.player
            if app.player == "red":
                app.player = "yellow"
            else:
                app.player = "red"
            winner = isWinner(app)
            if winner != None:
                app.winner = winner
                app.gameOver = True
            return
    # No spots available
    app.invalidCol = True
    
def redrawAll(app):
    drawBoard(app)
    drawLabel(f"{app.player}'s turn", app.width/2, app.height-80, size=40)
    
    if app.gameOver:
        drawLabel(f"The winner is {app.winner}", app.width/2, app.height-40, size=40)
    elif app.invalidCol:
        drawLabel("Invalid column, try again", app.width/2, app.height-40, size=40)
    
runApp(800,800)