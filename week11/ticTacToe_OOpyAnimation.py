from cmu_graphics import *

class ticTacToe(object):
    
    def __init__(self):
        
        self.board= "0 1 2 3 4 5 6 7 8".split() # will make it a list to be able to modify it later
        self.symbols=["X", "O"]
        self.player= 0
        
    def makeMove(self, move):
        print(f" Player {self.player} move {move}")
        print("validMove? ", self.isValidMove(move))
        
        if self.isValidMove(move):
            self.board[move]= self.symbols[self.player]
            #self.switchPlayer()
            
    def isValidMove(self, move):
        if not (move >= 0 and move <=8):
            return False
        
        if str(move) in self.board:
            return True
        
        return False
    
    
    def switchPlayer(self):
        self.player= 1-self.player
        

    def getResult(self):
        
        #Case 1: 1 winner
        # ROWS
        if self.board[0] == self.board[1] and self.board[1] == self.board[2]:
            return 1
        
        if self.board[3] == self.board[4] and self.board[4] == self.board[5]:
            return 1
        
        if self.board[6] == self.board[7] and self.board[7] == self.board[8]:
            return 1
        
        # COLUMNS
        if self.board[0] == self.board[3] and self.board[3] == self.board[6]:
            return 1
        
        if self.board[1] == self.board[4] and self.board[4] == self.board[7]:
            return 1
        
        if self.board[2] == self.board[5] and self.board[5] == self.board[8]:
            return 1
        
        
        # Diagonals
        if self.board[0] == self.board[4] and self.board[4] == self.board[8]:
            return 1
        
        if self.board[2] == self.board[4] and self.board[4] == self.board[6]:
            return 1

    
        # Case 2: Game not finished
        for c in self.board:
            if c in "012345678":
                return 0
            
        # Case 3: No winner    
        return 2
            
            
        
        
        
        

### TEST 1
        
b= ticTacToe()

print(b.board)
b.makeMove(3) #X
print(b.board)

b.makeMove(1)#O
print(b.board)

b.makeMove(3)#X INVALID
print(b.board)

### Test 2
print("result: ", b.getResult())

b.makeMove(0) #X

b.makeMove(7) #O

b.makeMove(2) #X

b.makeMove(4) #O
print(b.board)

print("result: ", b.getResult())



################ ANIMATIONS

class Cell(object):
    
    #attributes: x, y, width, height, label
    #actions: draw, updateLabel, isClicked

    cellID= 0
    
    def __init__(self, x, y, width, height):
        self.x= x
        self.y= y
        self.width= width
        self.height= height
        self.label= None
        self.ID= Cell.cellID
        Cell.cellID+=1
        
    def updateLabel(self, l):
        self.label=l
        
    def isClicked(self, x, y):
        return (self.x <= x <= self.x + self.width) and (self.y <= y <= self.y+self.height)
    
    def draw(self):
        drawRect(self.x,self.y,self.width, self.height, border='black', fill=None)
        
        if self.label:
            if self.label=="X":
                color= "green"
            else: color= "red"
            
            drawLabel(self.label, self.x+self.width//2, self.y+ self.height//2, fill=color, size=0.5*self.width)
        

def reset(app):
    Cell.cellID=0
    
    app.cells=[]
    app.game= ticTacToe()
    app.result=0
    
    width= app.width//3
    height= app.height//3
    
    for i in range(3):
        for j in range(3):           
            c= Cell(j*width,i*height, width, height)
            app.cells.append(c)
            
def onAppStart(app):
    reset(app)
    
def onMousePress(app, x, y):
    
    if app.result!=0:
        return
    
    # 1) Detect Action
    for c in app.cells:
        if c.isClicked(x,y):
            break
        
    # 2) Process Action
    if app.game.isValidMove(c.ID):
        app.game.makeMove(c.ID) # Make Move & Switch Players
        c.updateLabel(app.game.symbols[app.game.player])  # 2) Display the Symbol on the Board       
        app.result= app.game.getResult()        
        app.game.switchPlayer()



def onKeyPress(app, key): 
     if key in "Rr":
        reset(app)
        
        
def redrawAll(app):
    
    for c in app.cells:
        c.draw()

    if app.result==1:
        player= app.game.symbols[1-app.game.player] 
        drawLabel(player+" is WINNER ", app.width//2, app.height-20, size= 20, fill="blue")
        
    elif app.result==2:
        drawLabel("NO WINNER ", app.width//2, app.height-20, size= 20, fill="blue")


runApp(width=800, height=800)
