def oddValues(L):
    
    #BC
    if not L:
       return []
    
    ol= oddValues(L[1:])
    if L[0]%2 == 1:
        return [L[0]]+ ol
    else:
        return ol
    
    
assert oddValues([1,3, 4, 9, 7, 8]) == [1,3,9,7]

# same Length
def interleave(L1, L2):
    if not L1: #len(L1) == 0
        return L2
    
    return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

assert interleave([1,3,5], [2,4,6]) == [1,2,3,4,5,6]


def interleave_DiffLen(L1, L2):
    
    if not L1:
        return L2
    
    if not L2:
        return L1
    
    return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

assert interleave_DiffLen([1,3,5], [2,4,6,7,8]) == [1,2,3,4,5,6,7,8]

def moreLetters(s, p=1):
    if len(s) == 0:
        return ""
    
    return s[0]*p + moreLetters(s[1:], p+1)

print(moreLetters("Hey"))


def reverseString(s):
   if not s:
       return s
   
   return s[-1]+reverseString(s[:-1])
   

assert reverseString("Hello") == "olleH"

def DC(s):
    if len(s) < 2:
        return s
    
    mid = len(s)//2
    return DC(s[mid:]) + DC(s[:mid])

assert DC("Hello") == "olleH"

print("Passed !")