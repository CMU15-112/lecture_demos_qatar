
def recSumPairs(L, i=0):
    print(" "*i, L)
    if len(L) <= 1:
        return [ ]
    porint
    return [L[0] + L[1]] + recSumPairs(L[1:], i+1)


    
        
print(recSumPairs([1,2,3,4]) )