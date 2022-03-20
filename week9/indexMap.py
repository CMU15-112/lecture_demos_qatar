"""
Without using iteration write the function indexMap(L)
that takes a 1D list L and returns a dictionary that maps each value in L to a set of the indexes in L
where that value occurs. For example:
"""


def indexMap(L, depth=0):
    print("   "*depth, f"indexMap({L})")
    if L == []:
        return {}
    res = indexMap(L[:-1], depth+1)
    e = L[-1]
    ix = len(L)-1
    if e in res:
        res[ e].add(ix)
    else:
        res[e] = { ix }
    print("   "*depth,  "-->", res)
    return res
    
    # index of last: len(L)-1
    # element L[-1]
    
    
    
assert(indexMap([5, 6, 5]) == { 5:{0,2}, 6:{1} })
assert(indexMap([9, 6, 3, 6, 9]) == { 3:{2}, 6:{1,3}, 9:{0,4} })
assert(indexMap([3, 2, 1, 3, 2, 3]) == { 1:{2}, 2:{1, 4}, 3:{0,3,5} })

{ 1:{2}, 2:{1, 4}, 3:{0,3, 5} }