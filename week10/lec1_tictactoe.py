from cmu_112_graphics import *

######## Tic-Tac-Toe Class ############
def areWinningMoves(L):
    return L[0] != None and L.count(L[0]) == len(L)

def extractColumn(board, col):
    L = []
    for i in range(len(board)):
        L.append(board[i][col])
    return L

class TicTacToeGame(object):
    
    def __init__(self):
        self.board = [ [None, None, None],
                       [None, None, None],
                       [None, None, None] ]
        # 0 1 2
        # 3 4 5
        # 6 7 8
        
        # Example: Location 3 is coordinate [1,0]
        
    def __repr__(self):
        ret = ""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == None:
                    ret += " "
                else:
                    ret += (str(self.board[i][j]))
                if j != 2:
                    ret += "|"
            if i != 2:
                ret += "\n"
                ret += "------\n"
        return ret
    
    # Make a move by placing marker at the location
    # Returns True if the move was placed, and False otherwise
    def makeMove(self, loc, marker):
        if loc < 0 or loc > 8:
            return False
        
        if marker != "X" and marker != "O":
            return False
        
        row = loc // 3
        col = loc % 3
        
        if self.board[row][col] != None:
            return False
        
        self.board[row][col] = marker
        
        return True
    
    def isBoardFull(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == None:
                    return False
        return True
    
    def isGameWon(self):
        # Check the horizontals
        for i in range(len(self.board)):
            if areWinningMoves(self.board[i]):
                return True
        
        # Check the verticals
        for j in range(len(self.board[0])):
            tmp = extractColumn(self.board, j)
            if areWinningMoves(tmp):
                return True
            
        # Check the upper left to lower right diagonal
        tmp = []
        for i in range(len(self.board)):
            tmp.append(self.board[i][i])
        if areWinningMoves(tmp):
            return True
        
        # Check the upper right to lower left diagonal
        tmp = []
        r = 0
        c = len(self.board)-1
        while c >= 0:
            tmp.append(self.board[r][c])
            r += 1
            c -= 1
        if areWinningMoves(tmp):
            return True        
            
        return False

######## Drawing helper functions ##########

def getBoxBounds(r, c, width, height):
    margin = min(width,height)//12
    
    boxWidth = (width - 2*margin) / 3
    boxHeight = (height - 2*margin) / 3
    
    x0 = margin + c * boxWidth
    y0 = margin + r * boxHeight
    x1 = x0 + boxWidth
    y1 = y0 + boxHeight
    return (x0,y0,x1,y1)

def drawGrid(canvas, app):
    width = app.width
    height = app.height
    for r in range(3):
        for c in range(3):
            x0,y0,x1,y1 = getBoxBounds(r, c, width, height)
            fillColor = None
            if r == app.hr and c == app.hc:
                fillColor = "yellow"
            canvas.create_rectangle(x0,y0,x1,y1,fill=fillColor)

def placeMoves(canvas, width, height, board):
    for r in range(3):
        for c in range(3):    
            letter = board[r][c]
            x0,y0,x1,y1 = getBoxBounds(r, c, width, height)
            x = (x0+x1)/2
            y = (y0+y1)/2
            canvas.create_text(x, y, text=letter, font="Arial 40 bold")
            
def drawTicTacToe(app, canvas):
    width = app.width
    height = app.height
    board = app.game.board
    
    drawGrid(canvas, app)
    placeMoves(canvas, width, height, board)

######## Animation code ##########

def appStarted(app):
    app.game = TicTacToeGame()
    app.hr = 0
    app.hc = 0

def keyPressed(app, event):
    if not app.game.isGameWon() and not app.game.isBoardFull():
        if event.key == "Right":
            app.hc = (app.hc + 1)%3
        elif event.key == "Down":
            app.hr = (app.hr + 1)%3
        elif event.key == "Left":
            app.hc = (app.hc - 1)%3
        elif event.key == "Up":
            app.hr = (app.hr - 1)%3
        elif event.key.lower() == "x":
            app.game.makeMove(3*app.hr+app.hc, "X")
        elif event.key.lower() == "o":
            app.game.makeMove(3*app.hr+app.hc, "O")

def redrawAll(app, canvas):
    drawTicTacToe(app, canvas)
    if app.game.isGameWon():
        canvas.create_text(app.width/2, 35,
                       text='Game over!', font='Arial 30 bold')
    elif app.game.isBoardFull():
        canvas.create_text(app.width/2, 35,
                       text='Tie!', font='Arial 30 bold')

runApp(width=800, height=800)