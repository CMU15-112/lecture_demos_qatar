def isValidSquare(L):
    if not isinstance(L, list):
        return False
    
    if L == [] or L[0] == []:
        return False
    
    # Checking that all rows have the same length, the number of rows
    target = len(L)
    for row in L:
        if not isinstance(row, list):
            return False
        if len(row) != target:
            return False
    
    # Make sure all items inside the 2d list are ints
    for row in L:
        for item in row:
            if not isinstance(item, int):
                return False
    
    # Check uniqueness
    alreadySeen = []
    for row in L:
        for item in row:
            if item in alreadySeen:
                return False
            alreadySeen.append(item)
            
def isMagic(L):
    target = sum(L[0])
    # Check rows
    for row in L:
        if sum(row) != target:
            return False
     
    # Check cols
    for c in range(len(L[0])):
        temp = []
        for r in range(len(L)):
            temp.append(L[r][c])
        if sum(temp) != target:
            return False
        
    # Check diag 1
    temp = []
    for i in range(len(L)):
        temp.append(L[i][i])
    if sum(temp) != target:
        return False
    
    # Check diag 2
    temp = []
    for i in range(len(L)):
        temp.append(L[i][len(L)-i-1])
    if sum(temp) != target:
        return False
    
    return True

def isMagicSquare(L):
    if isValidSquare(L) and isMagic(L):
        return True
    else:
        return False