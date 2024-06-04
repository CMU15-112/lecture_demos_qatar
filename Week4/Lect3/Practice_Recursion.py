def sum1ToN(n):
    if n ==1:
        return n
    
    return n+sum1ToN(n-1)

assert sum1ToN(4)==10


def maxDigit(n):
    if n < 10:
        return n
    
    return max(n%10, maxDigit(n//10))
    
assert maxDigit(2344329857320) == 9

def sumList(L):
    if L == []:
        return 0
    
    #if len(L) == 1:
        #return L[0]
    
    return L[0] + sumList(L[1:])

assert sumList([1,12, 13, 14, 19]) == sum([1, 12, 13, 14, 19])
assert sumList([]) == 0
    
print("Passed !!")

