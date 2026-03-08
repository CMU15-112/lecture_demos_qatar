def sumDigits_Iterative(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

def sumDigits(n):
    if n < 10:
        return n
    return n%10 + sumDigits(n//10)

assert sumDigits(432879) == 33
assert sumDigits_Iterative(432879) == 33

def sum1ToN(n):
    if n == 1:
        return n
    
    return n+sum1ToN(n-1)

assert sum1ToN(4)==10


def maxDigit(n):
    
    if n < 10:
        return n
    
    return max(maxDigit(n//2), n%10)
    
    
assert maxDigit(2344329857320) == 9

def sumList(L):
    
    if L == []:
        return 0
    
# fails if the list is empty    
#     if len(L)==1: 
#         return L[0]
    
    return L[0]+sumList(L[1:])


assert sumList([1,12, 13, 14, 19]) == sum([1, 12, 13, 14, 19])
assert sumList([]) == 0
 
def maxValue(L):
    # edge case
    if len(L) == 0:
        return None
    
    # Base Case
    if len(L) == 1:
        return L[0]
    
    
    maxV = maxValue(L[1:])
    return max(L[0], maxV)

assert maxValue([2,13,14,9])==14
assert maxValue([]) == None


def largestConsPairsSum(L):
    if len(L) < 2:
        return None
    
    if len(L) == 2:
        return L[0]+L[1]
      
    return max(L[0]+L[1], largestConsPairsSum(L[1:]))

assert largestConsPairsSum([1,2,3,4]) == 7


print("Passed !!")
