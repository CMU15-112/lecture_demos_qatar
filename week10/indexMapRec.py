#
def indexMapAux(L, res, ix, depth=0):
    #print("   "*depth, f"indexMapAux({L}, {D}, {ix} )")
    if L==[]:
        return

    if L[0] in D:
        res[L[0]].add(ix)
    else:
        res[L[0]] = {ix}

    indexMapAux(L[1:], res, ix+1, depth+1)



def indexMap(L):
    res = {}
    indexMapAux(L, res, 0)
    return res


assert(indexMap([5, 6, 5]) == { 5:{0,2}, 6:{1} })
assert(indexMap([9, 6, 3, 6, 9]) == { 3:{2}, 6:{1,3}, 9:{0,4} })
assert(indexMap([3, 2, 1, 3, 2, 3]) == { 1:{2}, 2:{1, 4}, 3:{0,3,5} })
