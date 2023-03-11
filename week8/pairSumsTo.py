# Find two elements of the list that sum to n
# If no pair exists, return None
def pairSumsToNv0(L, n):  # O(N^2)
    for n1 in L: # loop N times
        for n2 in L:  # loop N times (nested)
            if n1 + n2 == n:
                return (n1, n2)
    return None

def pairSumsToNv1(L, n):  # still O(N^2)
    for n1 in L: # Loop N times
        if n-n1 in L:  # this is O(N)
            return (n1, n-n1)
    return None
    
def pairSumsToNv2(L, n):  # O(N)
    mySet = set(L)
    for n1 in L:   # loop N times
        if n-n1 in mySet:   # this is O(1)
            return (n1, n-n1)
    return None
