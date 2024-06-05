def maxValue(L):
    
    if len(L) == 0:
        return None
    
    if len(L) == 1:
        return L[0]
    
    maxVal= maxValue(L[1:])
    return max(L[0], maxVal)

assert maxValue([2,13,14,9])==14
assert maxValue([]) == None

def largestConsPairsSum(L):
    if len(L) < 2:
        return None
    
    if len(L) == 2:
        return L[0]+L[1]
    
    currS= L[0]+L[1]
    largest = largestConsPairsSum(L[1:])
    return max(currS, largest)

assert largestConsPairsSum([1,2,3,4]) == 7


def oddValues(L):
    
    if not L:
        return []
    
    if L[0]%2==1:
        result= [L[0]] + oddValues(L[1:])
        return result
    else:
        return oddValues(L[1:])
    
assert oddValues([1,3, 4, 9, 7, 8]) == [1,3,9,7]

# same Length
def interleave(L1, L2):
    
    #if len(L1)==1:
        #return [L1[0], L2[0]]
    if len(L1) == 0:
        return L1
    
    result= [L1[0], L2[0]] + interleave(L1[1:], L2[1:])
    return result

def interleave_DiffLen(L1, L2):
    
    if not L1:
        return L2
    
    if not L2:
        return L1
    
    result= [L1[0], L2[0]] + interleave_DiffLen(L1[1:], L2[1:])
    return result

assert interleave([1,3,5], [2,4,6]) == [1,2,3,4,5,6]
assert interleave_DiffLen([1,3,5], [2,4,6,7,8]) == [1,2,3,4,5,6,7,8]

def reverseString(s):
    
   # if len(s) <2:
    if s== "": 
        return s
    
    return s[-1] + reverseString(s[0:-1])

assert reverseString("Hello") == "olleH"

def DC(s):
    print(s)
   # if len(s) <2:
   # if s== "": 
   #     return s
    
    if len(s) < 2:
        return s[0]
    
    mid= len(s)//2
    
    return  DC(s[mid:])+DC(s[0:mid])

assert reverseString("Hello") == "olleH"
assert DC("Hello") == "olleH"

print("Passed !")