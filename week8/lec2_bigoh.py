import math


# FUNCTION FAMILY EXAMPLES


# O(1)
# Constant
def func1(lst):
    if len(lst) > 0: # O(1)
        return lst[0] # O(1)
    else:
        return None # O(1)

# O(log N)
# Logarithmic
def func2(n):
    sum = 0 # O(1)
    i = n # O(1)
    while i > 0: # O(log n)
        sum = sum + i # O(1)
        i = i // 2 # O(1)
    return sum # O(1)

# O(sqrt(n))
# Square root
def func3(lst):
    num = len(lst)
    if num < 2:
        return False
    result = True
    for i in range(2, int(math.sqrt(num))): 
        if num % i == 0:
            result = False
    return result

# O(N)
# Linear
def func4(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

# O(N log N)
# Linearithmic
def func5(lst):
    n = len(lst) # O(1)
    result = None
    for i in range(len(lst)): # N
        num = n
        while num > 0: # log N
            if lst[i] == num:
                result = lst[i]
            num = num // 2
    return result

# O(N^2)
# Quadratic
def func6(lst):
    result = True  
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                result = False
    return result

# Searching lst for item
# O(N)
def func7(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return None


# BIG O CALCULATION EXAMPLES

# Assume number of rows == number of cols == N

#O(N)
def isFullRow(data, row):
    for i in range(len(row)):
        if row[i] == data.emptyColor:
            return False
    return True
    
# O(N^2)
def removeFullRows(data):
    fullRows = []
    newBoard = []
    
    #O(N^2)
    for row in range(len(data.board)-1, -1, -1): #O(N)
        if isFullRow(data, data.board[row]): # O(N)
            fullRows.append(row) #O(1)
    data.score += len(fullRows) ** 2

    # O(N)
    for i in range(len(fullRows)): # O(N)
        newBoard.append([data.emptyColor] * data.cols)
    
    # O(N^2)
    for row in range(len(data.board)): #O(N)
        if row not in fullRows: # O(N) for in operation on list
            tempRow = copy.copy(data.board[row]) # O(N) for copy
            newBoard.append(tempRow)
    data.board = newBoard
    
# You do!
# O(N log N)
def bigOh3(lst):
    tmp = copy.copy(lst) # O(N)
    
    for i in range(len(lst)): #O(N)
        j = 1
        while j < len(lst): # O(log N)
            j *= 2 
        lst[i] = j
    print(tmp, lst) 