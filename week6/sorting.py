def selectionSortv1(a):
    n = len(a)
    sortedList = []
    for i in range(n):
        # we need to decide which element comes next
        nextelem = min(a)
        sortedList.append(nextelem)
        a.remove(nextelem)
    return sortedList


def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])
    
def selectionSortv2(a):
    n = len(a)
    for startIndex in range(n):
        # we need to decide which element comes next
        minIndex = startIndex
        for j in range(startIndex+1,n):
            if a[j] < a[minIndex]:
                minIndex = j
        # minIndex is the index of the minimum element
        # swap
        swap(a, startIndex, minIndex)
    return a

def selectionSortv3(a):
    n = len(a)
    for startIndex in range(n):
        # we need to decide which element comes next
        nextelem = min(a[startIndex:])
        minIndex = a.index(nextelem, startIndex)
        # minIndex is the index of the minimum element
        # swap
        swap(a, startIndex, minIndex)
    return a

def bubbleSort(a):
    n = len(a)
    end = n
    swapped = True
    while (swapped):
        swapped = False
        for i in range(1, end):
            if (a[i-1] > a[i]):
                swap(a, i-1, i)
                swapped = True
        end -= 1
    return a


def mergeSort(L):
    if len(L) < 2:
        return L
    # Finding the mid of the array
    mid = len(L)//2
    # Dividing the list elements
    leftL = mergeSort(L[:mid])
    # into 2 halves and sort them
    rightL = mergeSort(L[mid:])
    # now I should merge
    sortedList = []
    i = 0
    j = 0
    while i < len(leftL) and j < len(rightL):
        if leftL[i] < rightL[j]:
            sortedList.append(leftL[i])
            i+=1
        else:
            sortedList.append(rightL[j])
            j+=1
    if i < len(leftL):
        sortedList += leftL[i:]
    if j < len(rightL):
        sortedList += rightL[j:]
    return sortedList


def testSort(sortFn, n=None):
    import random
    import time
    f = open("randomNumbers.txt")
    a = [int(line.strip()) for line in f.readlines()]
    if n != None:
        a = a[:n]
    sortedA = sorted(a)
    startTime = time.time()
    a = sortFn(a)
    endTime = time.time()
    elapsedTime = endTime - startTime
    if a != sortedA:
        print(a)
    assert(a == sortedA)
    print("%20s n=%d  time=%6.3fs" % (sortFn.__name__, n, elapsedTime))
    
testSort(mergeSort, 10000)
