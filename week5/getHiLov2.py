import math

def getHiLoAux(L, minsofar=math.inf, maxsofar=-math.inf):
    if L==[]:
        return (minsofar, maxsofar)
    minsofar = min(minsofar, L[0])
    maxsofar = max(maxsofar, L[0])
    return getHiLo(L[1:], minsofar, maxsofar)
    
def getHiLo(L, minsofar=math.inf, maxsofar=-math.inf):
    if L==[]:
        return None
    return getHiLoAux(L)
   
        
    