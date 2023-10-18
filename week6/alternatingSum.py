def alternatingSum(L):
    result = 0
    for i in range(len(L)):
        if i%2 == 0:
            res = res + L[i]
        else:
            res = res - L[i]
    return res
        
        
def alternatingSumv2(L):
    return sum(L[::2]) - sum(L[1::2])


assert(alternatingSumv2([1,2,3,4]) == -2)