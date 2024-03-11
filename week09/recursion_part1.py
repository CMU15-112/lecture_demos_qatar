def sumDigits(n):
    if n < 10:
        return n
    return n%10 + sumDigits(n//10)

assert sumDigits(432879) == 33

def sum1toN(n):
    if n == 1:
        return 1
    return n + sum1toN(n-1)

print("Testing...", end="")
assert sum1toN(4) == 10
print(" done")

def maxDigit(n):
    if n < 10:
        return n
    maxD = maxDigit(n//10)
    return max(n%10, maxD)

print("Testing...", end="")
assert maxDigit(23443298573209543) == 9
print(" done")

def sumList(L):
    if len(L) == 0:
        return 0
    return L[0] + sumList(L[1:])

print("Testing...", end="")
assert sumList([2, 12, 13, 14, 19]) == sum([2, 12, 13, 14, 19])
assert sumList([]) == 0
print(" done")

def maxValue(L):
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[0]
    maxV = maxValue(L[1:])
    return max(L[0], maxV)

print("Testing...", end="")
assert maxValue([2, 12, 13, 14, 19]) == 19
assert maxValue([]) == None
print(" done")

def oddValues(L):
    if len(L) == 0:
        return []
    if L[0] % 2 == 0:
        return oddValues(L[1:])
    else:
        return [ L[0] ] + oddValues(L[1:])
        
print("Testing...", end="")
assert oddValues([2, 12, 13, 14, 19]) == [13,19]
print(" done")