# divide and conquer

def listSum(L, depth=0):
    print("   "*depth, "listSum(",L,"):")
    if (len(L) == 0):
        result = 0
    elif (len(L) == 1):
        result= L[0]
    else:
        mid = len(L)//2
        result = listSum(L[:mid], depth+1) + listSum(L[mid:], depth+1)
    print("   "*depth, "-->", result)
    return result
        
print(listSum([2,3,5,7,11])) # 28