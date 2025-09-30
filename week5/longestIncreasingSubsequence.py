
def lis(arr):
    arr_len=len(arr)
    T=[1]*arr_len
    print(T)
    for i in range(1, arr_len):
        for j in range(0,i):
            if arr[i]> arr[j]:
                T[i]=max(T[i], T[j]+1)
            print (i, j, T)
        print()
    return T

arr=[7, -4, -2, 3, 0, 2]

print ('Longest increasing subsequence is ', max(lis(arr)))