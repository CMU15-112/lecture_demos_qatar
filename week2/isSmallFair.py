
def isSmallFair(n):
    if type(n) != int:
        return False
    n = abs(n)
    if n > 9999 or n < 1000:
        return False
    d0 = n%10
    d1 = (n//10)%10
    d2 = (n//100)%10
    d3 = (n//1000)%10
    nEvens = 0
    if d0%2 == 0:
        nEvens += 1
    if d1%2 == 0:
        nEvens += 1
    if d2%2 == 0:
        nEvens += 1
    if d3%2 == 0:
        nEvens += 1
    return nEvens == 2
   
    

assert(isSmallFair(1000) == False)
assert(isSmallFair(-1000) == False)
assert(isSmallFair(1234))
#assert(isSmallFair(-1234))