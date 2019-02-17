# Basic Animation Framework

from tkinter import *

def findWordFromLocationInDir(board, word, row, col, dir):
    for i in range(len(word)):
        curRow = row+i*dir[0]
        curCol = col+i*dir[1]
        
        if curRow > len(board)-1 or curCol > len(board[0])-1 or \
           curRow < 0 or curCol < 0:
               return None
        
        #print(row, col, curRow, curCol, i, dir)
        if board[curRow][curCol] != word[i]:
            return None
    # I found the word
    return ( (row, col), (curRow, curCol) )
        

def findWordFromLocation(board, word, row, col):
    for dir in [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]:
        found = findWordFromLocationInDir(board, word, row, col, dir)
        if found != None:
            return found
        

def wordSearch(board, word):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if word[0] == board[row][col]:
                found = findWordFromLocation(board, word, row, col)
                if found != None:
                    return found

def solveGame(data):
    foundWords = []
    
    for word in data.words:
        found = wordSearch(data.board, word)
        print(word, found)
        if found != None:
            data.lines.append(found)
            foundWords.append(word)
    
    for word in foundWords:
        data.words.remove(word)

####################################
# customize these functions
####################################

def init(data):
    data.board = [   [ 'd', 'o', 'g' ],
                     [ 't', 'a', 'c' ],
                     [ 'o', 'a', 't' ],
                     [ 'u', 'r', 'k' ],
                 ]
    data.words = ["cat", "dog", "kat"]
    
    colWidth = data.width / len(data.board[0])
    rowWidth = data.height / len(data.board)
    
    data.cellWidth = min(colWidth, rowWidth)
    
    data.selected = []
    data.selectedWord = ""
    
    data.lines = []

def mousePressed(event, data):
    # use event.x and event.y
    row = int(event.y // data.cellWidth)
    col = int(event.x // data.cellWidth)

    if row >= 0 and row < len(data.board) and \
       col >= 0 and col < len(data.board[0]):
        data.selected.append((row, col))
        data.selectedWord += data.board[row][col]
        
        if data.selectedWord in data.words:
            print("Found a word!")
            
            data.lines.append( (data.selected[0], data.selected[-1]) )
            
            data.words.remove(data.selectedWord)
            data.selected = []
            data.selectedWord = ""
            
            
        
    else:
        data.selected = []
        data.selectedWord = ""

def keyPressed(event, data):
    # use event.char and event.keysym
    if event.char == "s":
        print("Initiating a solve")
        solveGame(data)
    pass

def drawBoard(canvas, data):
    for i in range(len(data.board)):
        for j in range(len(data.board[i])):
            left = data.cellWidth*j
            top = data.cellWidth*i
            
            if (i,j) in data.selected:
                color = "yellow"
            else:
                color = "lightblue"
            
            canvas.create_rectangle(left,top,left+data.cellWidth,
                                    top+data.cellWidth,
                                    fill=color)
            
            fontSize = int(data.cellWidth/2)
            canvas.create_text(left+data.cellWidth/2, top+data.cellWidth/2,
                               text=data.board[i][j], 
                               font="Arial "+str(fontSize))

    left = data.cellWidth*len(data.board[0])+10
    fontSize = int(data.cellWidth/4)                 
    for i in range(len(data.words)):
        canvas.create_text(left, i*data.cellWidth, 
                           text=data.words[i],
                           anchor="nw",
                           font = "Arial " + str(fontSize))    

def drawLines(canvas, data):
    
    for (start,end) in data.lines:
        print(start, end)
        canvas.create_line(start[1]*data.cellWidth+data.cellWidth//2, 
                           start[0]*data.cellWidth+data.cellWidth//2,
                            end[1]*data.cellWidth+data.cellWidth//2, 
                            end[0]*data.cellWidth+data.cellWidth//2)

def redrawAll(canvas, data):
    drawBoard(canvas, data)
    drawLines(canvas, data)


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    redrawAll(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(500, 500)