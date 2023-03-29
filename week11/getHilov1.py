def getHiLo(L, depth=0 ):
    print("   "*depth, "getHiLo(", L, " )")
    if len(L)==1:
        return (L[0], L[0])
    
    (a, b) = getHiLo(L[1:], depth+1)
    if L[0] < a:
        a = L[0]
    if L[0] > b:
        b = L[0]
    return (a, b)

assert(getHiLo([1,2,3,4,5]) == (1,5))