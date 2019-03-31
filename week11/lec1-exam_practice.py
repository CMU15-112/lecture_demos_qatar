def ct1(L, depth=0):
    print(depth, "in: ", L)
    
    # Magic size base case
    if (len(L) % 3 < 2):
        print(depth, "base case")
        res = L
    else:
        print(depth, "recursive case")
        k = len(L)//2 + 1
        # Recurse on first half of the list
        # Prepend sum of L to the return, then return that
        res = [sum(L), ct1(L[:k], depth+1)]
        
    print(depth, "out: ", res)
    return res
        
#L = [-1, 0, 1, 2] * 2
#print(ct1(L))

def ct2(n):
    if n < 10:
        return (n, n)
    else:
        (a, b) = ct2(n // 10)
        d = n % 10
        if d > a:
            a=d
        elif d < b:
            b=d
        return (a, b)
            
#print(ct2(3276))

def increasingPathCount(board, r=0, c=0):
    
    if r == len(board)-1 and c == len(board)-1:
        return 1
    else:
        cnt = 0
        for nextL in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
            nr, nc = nextL
            
            if nr < 0 or nr >= len(board):
                continue
            if nc < 0 or nc >= len(board):
                continue
            
            if board[nr][nc] > board[r][c]:
                cnt += increasingPathCount(board, nr, nc)
        return cnt
                
board = [[ 1, 3, 2, 4 ],
         [ 0, 4, 0, 3 ],
         [ 5, 6, 7, 8 ],
         [ 0, 7, 8, 9 ]]
               
print(increasingPathCount(board))