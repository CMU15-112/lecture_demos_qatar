
def destructiveRemoveNonInts(L):
    Lcopy = L[:]
    for e in Lcopy:
        if not isinstance(e, int):
            L.remove(e)
            
L = [112, '15', 4, 2, 'hey',  15.112]
assert(destructiveRemoveNonInts(L) == None)
assert(L == [112, 4, 2])