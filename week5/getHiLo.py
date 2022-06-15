"""
Write the recursive function getHiLo(lst)
which, given a list of integers lst returns a tuple
contain the highest and lowest values in the list.  For example:
getHiLo([1, 7, 3, 8, 2, 9, 6, 4, 5]) returns (9,1)
getHiLo([5]) returns (5,5)
getHiLo([]) returns None
"""

def getHiLo(L):
    if L=[]:
        return None
    else:
        (a, b) = getHiLo(L[1:])
        if L[0] < a:
            a = L[0]
        if L[0] > b:
            b = L[0]
        return (a,b)
    
# another solution, use helper functions!
    
def getMax(L):
    if len(L)==1:
        return L[0]
    return max(getMax(L[1:], L[0]))
def getMin(L):
    if len(L)==1:
        return L[0]
    return min(getMin(L[1:], L[0]))

def getHiLo(L):
    if L=[]:
        return None
    return (getMin(L), getMax(L))
    
    
def getHiLo(L):
    if L=[]:
        return None
    else:
        (a, b) = getHiLo(L[1:])
        if L[0] < a:
            a = L[0]
        if L[0] > b:
            b = L[0]
        return (a,b)
    