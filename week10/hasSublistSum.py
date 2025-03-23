def hasSublistSum(L, s):
    if s == 0:
        return True
    elif L == []: 
        return False
    else:
        return hasSublistSum(L[1:], s-L[0]) or hasSublistSum(L[1:], s)