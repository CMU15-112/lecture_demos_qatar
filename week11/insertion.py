
from random import randint

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    
def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0:
            if arr[j - 1] > arr[j]:
                swap(arr, j, j - 1)
                j -= 1
            else:
                break

L = [randint(0, 100) for i in range(10)]
print(L)
insertionSort(L)
print(L)