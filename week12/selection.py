from random import randint

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
                
def selectionSort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        swap(arr, i, minimum)
                
           
my_array = [randint(0, 100) for i in range(10)]
print(my_array)
selectionSort(my_array)
print(my_array)