def binarySearch(L, x):
    low = 0
    high = len(L)
    while low < high:  # while the interval is not empty
        mid = (high + low) // 2
        # If element is present at the middle itself
        if L[mid] == x:
            return True
        # If element is smaller than mid, then it can only
        # be present in left half
        elif x < L[mid]:
            high = mid
        # Else the element can only be present in right half
        else:
            low = mid+1
    return False