import math
def getHiLo(L, minsofar=math.inf, maxsofar=-math.inf, depth=0):
    print("   "*depth, f"getHiLo({L}, {minsofar}, {maxsofar} )")
    if len(L)==0:
        return (minsofar, maxsofar)
    
    if L[0] < minsofar:
        minsofar = L[0]
    if L[0] > maxsofar:
        maxsofar = L[0]
    return getHiLo(L[1:], minsofar, maxsofar, depth+1)

assert(getHiLo([1,2,3,4,5]) == (1,5))