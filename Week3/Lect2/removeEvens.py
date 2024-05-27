def removeEvensDestructive(L):  
    for e in L[:]:
        if e%2==0:
            L.remove(e)
            
            
    
def removeEvensNonDestructive(L):
    newL= []
    for e in L:
        if e%2 != 0:
            newL.append(e)
            
    return newL
            
    

L= [54, 21, 42, 76, 33]
assert(removeEvensNonDestructive(L) == [21, 33])

removeEvensDestructive(L)
assert(L == [21, 33])

