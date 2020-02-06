def printGame(b):
    print (b[0] + "|"+b[1]+"|"+b[2])
    print ("-----")
    print (b[3] + "|"+b[4]+"|"+b[5])
    print ("-----")
    print (b[6] + "|"+b[7]+"|"+b[8])
def makeMove(b,i,symb):
    if 0 <= i and i <= 8:
        if b[i].isdigit():
            b[i] = symb
            return True
    return False

# returns 0 if continue
# returns 1 if result
# returns 2 if tie
def getResult(b):
    #check rows
    for i in range(3):
        if b[i*3] == b[i*3+1] == b[i*3+2]:
            return 1
    #check cols
    for i in range(3):
        if b[i] == b[i+3] == b[i+6]:
            return 1
    if b[0] == b[4] == b[8]:
        return 1
    if b[2] == b[4] == b[6]:
        return 1
    
    for c in b:
        if c.isdigit():
            return 0
    return 2



board = "1 2 3 4 5 6 7 8 9".split()

printGame(board)
player = 'X'
while getResult(board) == 0:
    move = int(input("Make your move"))
    while makeMove(board,move-1,player) == False:
        move = int(input("Make your move"))
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    printGame(board)

if getResult(board) == 2:
    print ("game ended in a tie")
else:
    print(player," Lost the game")
    

















 
