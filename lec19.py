def fib(n,fibs):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in fibs:
        return fibs[n]
    r = fib(n-1,fibs) + fib(n-2,fibs)
    fibs[n] = r
    return r

def isBalancedHelper(s,count):
    print(count,s)
    if count == -1:
        return False
    if s == "" and count == 0:
        return True
    if s == "" and count != 0:
        return False
    if s[0]== "(":
        return isBalancedHelper(s[1:],count+1)
    if s[0] == ")":
        return isBalancedHelper(s[1:],count -1)
    
    return isBalancedHelper(s[1:],count)
def isBalancedH(s):
    if s == "":
        return 0
    if s[0] == "(":
        r = 1 + isBalancedH(s[1:])
        if r > 0:
            return 10000000000
        return r
    if s[0] == ")":
        r = -1 + isBalancedH(s[1:])
        return r
    r = isBalancedH(s[1:])
    return r
    
    
def isBalanced(s):
    if s == "":
        return True
    return isBalancedH(s) == 0


def ToH(n,From,To,Temp):
    if n == 1:
        print (From," -- >", To)
    else:
        ToH(n-1,From,Temp,To)
        print (From," -- >", To)
        ToH(n-1,Temp,To,From)
        

ToH(3,"A","C","B")
#print (fib(50,{}))
#print (isBalanced("A"))
#print (isBalanced("(A)"))
print (isBalanced("(A+3)+2)+4)"))
#print (isBalanced("()(A))"))
#print (isBalanced("()()()((()))(A)"))
#print (isBalanced("(3 + 4 + 5(-5+8))"))
#print (isBalanced("3 + 4 + 5(-5+8))"))













