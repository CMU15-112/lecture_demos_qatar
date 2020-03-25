def dimension(board):
    a = len(board)
    b = a ** 0.5
    return int(b)

def printBoard(board):
    numCols = dimension(board)
    numRows = len(board)//numCols
    
    for row in range(numRows):
        for col in range(numCols):
            print(board[col + numRows*row], end=" ")
            if col < numCols-1:
                print("| ", end="")
        print()
        if row < numRows-1:
            print("---------")

startingBoard = "X X O O X O X O X".split(" ")
printBoard(startingBoard)