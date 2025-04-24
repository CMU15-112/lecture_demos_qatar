def extractCols(M, cols):
    # L[..][j]
    res = []
    for i in range(len(M)):
        newrow = []
        for j in range(len(cols)):
            # add M[i][col[j]]
            newrow.append(M[i][col[j]])
        res.append(newrow)
    return res
        



M1 = [ [1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9] ] 
      
cols1 = [2, 0]

assert extractColumns(M1, cols1) == [ [3, 1], 
                                      [6, 4], 
                                      [9, 7] ] 
M2 = [ [1, 2],
       [3, 4] ]
       
cols2 = [0, 1, 0, 1]

assert extractColumns(M2, cols2) == [ [1, 2, 1, 2],
                                      [3, 4, 3, 4] ]