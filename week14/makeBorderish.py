def isBorderish(L):
    # sum border, inside, compare
    innerSum = 0
    for row in L[1:-1]:
        innerSum += sum(row[1:-1])
    totalsum= 0
    for row in L:
        totalsum += sum(row)
    outside = totalsum - innersum
    return innersum == outside
        

def swapColumns(L, i, j):
    Lcopy = copy.deepcopy(L)
    for row in Lcopy:
        row[j], row[i] = row[i], row[j]
    return Lcopy

def makeBorderish(L):
    NROWS = len(L)
    NCOLS = len(L[0])
    for i in range(NCOLS):
        for j in range(NCOLS):
            if ( isBorderish(swapColumns(L, i, j))):
                # if I swap i and j, i make it borderish
                for row in L:
                    row[j], row[i] = row[i], row[j]
                return

                
            
                
            