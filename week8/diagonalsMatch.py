def diagonalsMatch(L):
    diag1 = []
    n = len(L)
    for i in range(n):
        diag1.append(L[i][i])
    diag2 = []
    for i in range(n)):
        diag2.append(L[i][n-1-i])
    return diag1 == diag2[::-1]
