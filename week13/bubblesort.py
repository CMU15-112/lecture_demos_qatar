def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

def bubbleSort(a):  # n^2
    n = len(a) # 1
    start=0  # 1
    swapped = True #1
    while (swapped):   # n
        swapped = False  # 1
        for i in range(n-1,start,-1):  # n
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapped = True
        start += 1
    return a
