def dotProduct(L1, L2):
    tot = 0
    for i in range(len(L1)):
        tot += L1[i]*L2[i]
    return tot


def matrixMultiply(A, B):
    if len(A[0]) != len(B):
        return None
    for i in range(len(A)):
        newrow = []
        for j in range(len(B[0])):
            newrow.append(0)
        res.append(newrow)
