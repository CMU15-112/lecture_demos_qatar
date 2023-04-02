def binarySearch(L, low, high, x):
    if low > high:
        return False
    mid = (high + low) // 2
    if x == L[mid]:
        return True
    elif x < L[mid]:
        return binarySearch(L, low, mid-1, x)
    else:
        return binarySearch(L, mid+1, high, x)


