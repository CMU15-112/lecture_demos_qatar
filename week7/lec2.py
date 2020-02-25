# Normal solution
def hasMatchingParenthesis(s):
    numOpen = 0
    numClosed = 0
    
    for c in s:
        if c == "(":
            numOpen += 1
        elif c== ")":
            numClosed += 1
        
        if numClosed > numOpen:
            return False
            
    return numOpen == numClosed

# Slightly better solution
def hasMatchingParenthesis(s):
    cnt = 0
    
    for c in s:
        if c == "(":
            cnt += 1
        elif c== ")":
            cnt -= 1
        
        if cnt < 0:
            return False
            
    return cnt == 0

# Recursive solution
def hasMatchingParenthesis(s, cnt=0):    
    if len(s) == 0:
        return cnt == 0
    else:
        if s[0] == "(":
            cnt += 1
        elif s[0] == ")":
            cnt -= 1
        if cnt < 0:
            return False
        
        # Do something recursive
        return hasMatchingParenthesis(s[1:], cnt)

print("Testing hasMatchingParenthesis...", end="")
assert( hasMatchingParenthesis("(2+4)/5") == True )
assert( hasMatchingParenthesis("(2+(4-3))/5") == True )
assert( hasMatchingParenthesis("(( cat( )dog))") == True )
assert( hasMatchingParenthesis("((purple ())") == False )
assert( hasMatchingParenthesis("() ) ((fred)") == False )
print("done")

def fib(n, depth=0):
    print(" "*depth, "fib("+str(n)+")")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1, depth+1) + fib(n-2, depth+1)
    
print(fib(7))