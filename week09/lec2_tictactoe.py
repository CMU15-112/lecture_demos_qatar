import basic_graphics

def getBoxBounds(r, c, width, height):
    margin = min(width,height)//12
    
    boxWidth = (width - 2*margin) / 3
    boxHeight = (height - 2*margin) / 3
    
    x0 = margin + c * boxWidth
    y0 = margin + r * boxHeight
    x1 = x0 + boxWidth
    y1 = y0 + boxHeight
    return (x0,y0,x1,y1)

def drawGrid(canvas, width, height):
    for r in range(3):
        for c in range(3):
            x0,y0,x1,y1 = getBoxBounds(r, c, width, height)
            canvas.create_rectangle(x0,y0,x1,y1)

def placeMoves(canvas, width, height, board):
    for r in range(3):
        for c in range(3):    
            letter = board[r][c]
            x0,y0,x1,y1 = getBoxBounds(r, c, width, height)
            x = (x0+x1)/2
            y = (y0+y1)/2
            canvas.create_text(x, y, text=letter, font="Arial 40 bold")
            
def drawTicTacToe(canvas, width, height, board):
    drawGrid(canvas, width, height)
    placeMoves(canvas, width, height, board)

def draw(canvas, width, height):
    board = [ ["X", None, "O"],
              ["X", "X", None],
              ["O", "O", "X"] ]
    drawTicTacToe(canvas, width, height, board)
    

basic_graphics.run(width=800, height=800)