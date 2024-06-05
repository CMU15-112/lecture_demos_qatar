def ctHelper(L, r, c):
    print(L[r][c])
    lim = len(L)
    if r + 1 < lim and L[r + 1][c] % 2 == 1:
        ctHelper(L, r + 1, c)
    if c + 1 < lim and L[r][c + 1] % 2 == 1:
        ctHelper(L, r, c + 1)

def ct4(L):
    ctHelper(L, 0, 0)

L = [
        [3, 2, 4],
        [9, 7, 5],
        [1, 6, 11]
    ]
ct4(L)