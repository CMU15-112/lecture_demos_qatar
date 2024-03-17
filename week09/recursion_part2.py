from functools import cache

def interleave(list1, list2):
    if len(list1) == 0:
        return []
    return [list1[0], list2[0]] + interleave(list1[1:], list2[1:])

print("Testing...",end="")
assert interleave([1,2,3],[10,11,12]) == [1,10,2,11,3,12]
print("done")

def interleaveAgain(list1, list2):
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    return [list1[0], list2[0]] + interleaveAgain(list1[1:], list2[1:])

print("Testing...",end="")
assert interleaveAgain([1,2,3,4,5],[10,11]) == [1,10,2,11,3,4,5]
print("done")

def stringReverse(s):
    if s == "":
        return ""
    return stringReverse(s[1:]) + s[0]

print("Testing...",end="")
assert stringReverse("hithere") == "erehtih"
print("done")

def stringReverse(s):
    if s == "":
        return ""
    return s[-1] + stringReverse(s[0:-1])

print("Testing...",end="")
assert stringReverse("hithere") == "erehtih"
print("done")

def reverseThing(t):
    if len(t) == 0:
        return t
    if type(t) == str:
        return t[-1] + reverseThing(t[0:-1])
    else:
        return [t[-1]] + reverseThing(t[0:-1])

print("Testing...",end="")
assert reverseThing("hithere") == "erehtih"
assert reverseThing([1,2,3]) == [3,2,1]
print("done")

def reverseDC(s):
    #print(s)
    if len(s) == 0:
        return ""
    elif len(s) == 1:
        return s[0]
    midPoint = len(s)//2
    return reverseDC(s[midPoint:]) + reverseDC(s[0:midPoint])

print("Testing...",end="")
assert reverseDC("hithere") == "erehtih"
print("done")

fibCache = dict()
def fib(n, d = 0):
    if n in fibCache:
        return fibCache[n]
    #print(" "*d, n)
    if n < 2:
        res = 1
    else:
        res = fib(n-1, d+1) + fib(n-2, d+1)
        
    fibCache[n] = res
    return res

@cache
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(300))

def findItemPairs(L, item):
    if len(L) == 1:
        return [(item, L[0])]
    return [(item, L[0])] + findItemPairs(L[1:], item)

assert findItemPairs([2,3,4],1) == [(1, 2), (1, 3), (1, 4)]

def allPairs(L):
    if len(L) == 2:
        return [tuple(L)]
    return findItemPairs(L[1:], L[0]) + allPairs(L[1:])

print(allPairs([1,2,3,4]))
    