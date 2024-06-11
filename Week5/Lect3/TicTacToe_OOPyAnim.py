from cmu_graphics import *


########################### CLASSES ##############################

class Cell(object):
    
    nextID= 0
    def __init__(self):
        self.ID= Cell.nextID
        Cell.nextID+=1
        self.label = str(self.ID)
        
    def __repr__(self):
        return f"{self.label}"
    
    def setCoords(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def draw(self):
        
        if self.label != str(self.ID):
            if self.label == "X":
                c= "green"
            else:
                c= "red"
            drawLabel(f"{self.label}", self.x+self.w//2, self.y+self.h//2, size= self.w//2, fill=c)
            
        drawRect(self.x,self.y,self.w,self.h, fill= None, border= "black")
        
    def isClicked(self, x, y):
        return (self.x <= x <= self.x+self.w) and (self.y <= y <= self.y+self.h)

class tictactoe(object):
    
    def __init__(self):
        self.board = []
        Cell.nextID = 0# reset it to 0 each time
        for i in range(9):
            self.board.append(Cell())
            
        self.playSymbols= ["X", "O"]
        self.currPlayer= 0 #1
            
    def isValidMove(self, cellID):
        return (0<= cellID <= 8) and (self.board[cellID].label.isdigit())
        
    def switchPlayer(self):
        self.currPlayer = (self.currPlayer+1)%2
        
    def move(self, cellID):
        if self.isValidMove(cellID):
            self.board[cellID].label = self.playSymbols[self.currPlayer]
            self.switchPlayer()
            
    def getStatus(self):
        #Case 1: 1 winner
        # ROWS
        if self.board[0].label == self.board[1].label  and self.board[1].label  == self.board[2].label:
            return 1
        
        if self.board[3].label == self.board[4].label and self.board[4].label == self.board[5].label:
            return 1
        
        if self.board[6].label == self.board[7].label and self.board[7].label == self.board[8].label:
            return 1
        
        # COLUMNS
        if self.board[0].label == self.board[3].label and self.board[3].label == self.board[6].label:
            return 1
        
        if self.board[1].label == self.board[4].label and self.board[4].label == self.board[7].label:
            return 1
        
        if self.board[2].label == self.board[5].label and self.board[5].label == self.board[8].label:
            return 1
        
        
        # Diagonals
        if self.board[0].label == self.board[4].label and self.board[4].label == self.board[8].label:
            return 1
        
        if self.board[2].label == self.board[4].label and self.board[4].label == self.board[6].label:
            return 1
        
        # game not finished
        for c in self.board:
            if c.label == str(c.ID): # at least one cell has the initial value
                return 0
        
        return 2 # no winner
    
    


########################### ANIMATIONS #########################
def reset(app):
    app.game= tictactoe()
    
    
    app.cW= app.width//3
    app.cH= app.height//3
    
    cID= 0
    for r in range(3):
        for c in range(3):
            cell = app.game.board[cID]
            cell.setCoords(c*app.cW, r*app.cH, app.cW, app.cH)
            cID+=1
            
    app.status = 0
    
    
    
def onAppStart(app):
    reset(app)
    
    
    
def onMousePress(app, x, y):
    
    if app.status!=0:
        return
    
    cell= -1
    for c in app.game.board:
        if c.isClicked(x,y):
            cell = c.ID
            break
    print("selected: ", cell)
    if cell >= 0:
        app.game.move(cell) 
        app.status = app.game.getStatus()
    
def onKeyPress(app, key): 
     if key in "rR":
         reset(app)
        
        
def redrawAll(app):
    
    for c in app.game.board:
        c.draw()
        
    if app.status == 1:
        winner = app.game.playSymbols[(app.game.currPlayer+1)%2]
        drawLabel(f"{winner} is a WINNER", app.width//2, app.height-20, size= 20, fill= "blue")
    elif app.status ==2:
        drawLabel("NO WINNER", app.width//2, app.height-20, size= 20, fill= "blue")


runApp(width=800, height=800)