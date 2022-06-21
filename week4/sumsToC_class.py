import time


# Find two elements of the list that sum to n
# If no pair exists, return None
# Example:
# pairSumsToN( [1,3,4,1,2], 2) == (1,1)
# pairSumsToN( [1,3,4,1,2], 10) == None
# pairSumsToN( [1,3,4,1,2], 6) == (3,3)


def pairSumsToNv0(L, n):
    for e1 in L:
        for e2 in L:
            if e1 + e2 == n:
                return (e1, e2)
    return None

def pairSumsToNv1(L, n):
    for e1 in L:
        if n-e1 in L:
            return (e1, n-e1)
    return None

def pairSumsToNv2(L, n):
    mySet = set(L)
    for e1 in L:
        if n-e1 in mySet:
            return (e1, n-e1)
    return None



    
    