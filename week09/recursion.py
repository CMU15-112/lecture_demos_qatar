def sumDigits(n):
    # Base Case
    if n < 10:
        return n
    
    # Recursive case
    lastDigit = n % 10
    result = lastDigit + sumDigits(n//10)
    return result

print(sumDigits(123))

# For example, sum1ToN(4) == 1 + 2 + 3 + 4
def sum1ToN(n):
    # Base Case
    if n <= 0:
        return 0
    #if n == 1:
    #    return 1
    
    # Recursive Case
    return sum1ToN(n-1) + n

print(sum1ToN(4))
print(sum1ToN(0))

# Return the largest digit in n
def maxDigit(n):
    # Base case
    if n < 10:
        return n
    
    last = n % 10
    rest = maxDigit(n//10)
    if last > rest:
        return last
    else:
        return rest
    #return max(n%10, maxDigit(n//10))
    
print(maxDigit(423678612412))
print(maxDigit(0))
print(maxDigit(919))

def sumList(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    #return lst[-1] + sumList(lst[:-1])
    return lst[0] + sumList(lst[1:])

print(sumList([1,2,3,4]))
print(sumList([]))

def maxValue(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    
    cur = lst[0]
    rest = maxValue(lst[1:])
    if cur > rest:
        return cur
    else:
        return rest

print(maxValue([]))
print(maxValue([432,423,12,643,624,3,2,665427546,8]))

# Return only the odd values of lst in the same order that they appear
# [1,2,3,4,3,2] -> [1,3,3]
def oddValues(lst):
    # Base Case
    if len(lst) == 0:
        return []
    
    # Recursive Case
    cur = lst[0]
    if cur % 2 == 1:
        return [cur] + oddValues(lst[1:])
    else:
        return oddValues(lst[1:])
    
print(oddValues([1,2,3,4,3,2]))
print(oddValues([]))
print(oddValues([1]))
print(oddValues([2]))

# Assume lst1 and lst2 are the same size
# Return an interleaved version of the both
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# then return [1, 4, 2, 5, 3, 6]
def interleave(lst1, lst2):
    if len(lst1) == 0:
        return []
    
    # Recursive
    return [lst1[0]]+ [lst2[0]] + interleave(lst1[1:], lst2[1:])

print(interleave([1, 2, 3], [4, 5, 6]))

def interleaveWeird(lst1, lst2):
    if len(lst1) == 0:
        return []
    
    return [lst1[0]]+interleaveWeird(lst2, lst1[1:])

print(interleaveWeird([1, 2, 3], [4, 5, 6]))

def interleaveHarder(lst1, lst2):
    # Base case
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    
    # Recursive
    return [lst1[0]]+ [lst2[0]] + interleaveHarder(lst1[1:], lst2[1:])

assert interleaveHarder([1, 2, 3], [15]) == [1, 15, 2, 3]
print(interleaveHarder([1, 2, 3], [15]))

def reverseString(s):
    if len(s) <= 1:
        return s
    
    # Recursive Case
    return s[-1] + reverseString(s[:-1])

print(reverseString("hithere"))
print(reverseString(""))
#print(reverseString("ab"*500))

def reverseDC(s):
    if len(s) <= 1:
        return s
    
    midPoint = len(s) // 2
    return reverseDC(s[midPoint:]) + reverseDC(s[:midPoint])

print(reverseDC("hithere"))
print(reverseDC(""))
print(reverseDC("abc"*500))

# Given a list of integers, returns a list of all the possible pairs of items in L.
# [1,2,3,4] -> [(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)]
def allPairs(L):
    if len(L) <= 1:
        return []
    pairs = findItemPairs(L[1:], L[0])
    return pairs + allPairs(L[1:])

def findItemPairs(L, item):
    if len(L) == 0:
        return []
    #if len(L) == 1:
    #    return [(L[0], item)]
    return [(L[0], item)] + findItemPairs(L[1:], item)

print(allPairs([1,2,3,4]))






