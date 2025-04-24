def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

def selectionSort(a):
    n = len(a) # O(1)
    for startIndex in range(n):  # O(n)
        # we need to decide which element comes next
        minIndex = startIndex  # O(1)
        for j in range(startIndex+1,n):  
            if a[j] < a[minIndex]:
                minIndex = j
        # minIndex is the index of the minimum element
        # swap
        swap(a, startIndex, minIndex)
    return a
