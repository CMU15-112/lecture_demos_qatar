def areWinningMoves(L):
    return L[0] != None and L.count(L[0]) == len(L)

def testAreWinningMoves():
    print(areWinningMoves(["X","X","X"]))
    print(areWinningMoves(["X","O","X"]))
    print(areWinningMoves(["X",None,"X"]))
    print(areWinningMoves([None,None,None]))

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
    
def testTicTacToe():
    g = TicTacToeGame()
    r = g.makeMove(4, "X")
    print(r)
    r = g.makeMove(0, "X")
    print(r)
#     r = g.makeMove(8, "X")
#     print(r)    
    r = g.makeMove(0, "X")
    print(r)
    r = g.makeMove(-1, "X")
    print(r)
    r = g.makeMove(9, "X")
    print(r)
    r = g.makeMove(2, "J")
    print(r)
    g.makeMove(1, "O")
    g.makeMove(3, "O")
    g.makeMove(2, "X")
    #g.makeMove(8, "X")
    g.makeMove(7, "X")
    g.makeMove(6, "X")
    
    print("Check for winner!", g.isGameOver())
    
    print(g)
    
    #print(extractColumn(g.board, 2))
    
g = TicTacToeGame()
current = "X"
while g.isGameWon() == False and g.isBoardFull() == False:
    print(g)
    print("========")
    inp = input(f"{current}, make your move: ")
    val = int(inp)
    g.makeMove(val, current)
    if current == "X":
        current = "O"
    elif current == "O":
        current = "X"
        
# More code needed to print out after game ends