
from random import randint

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
    
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

L = [randint(0, 100) for i in range(10)]
print(L)
bubbleSort(L)
print(L)
