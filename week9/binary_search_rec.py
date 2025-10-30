def binary_search_rec(L, target, low, high):
    if low > high:  # Base case: target not found
        return -1

    mid = low + (high - low) // 2
    #print(L[mid])

    if L[mid] == target: 
        return mid
    elif L[mid] > target:
        #print(L[low:mid])
        return binary_search_rec(L, target, low, mid - 1)
    else:
        #print(L[mid+1:high+1])
        return binary_search_rec(L, target, mid + 1, high)


sortedL = [2, 4, 9, 12, 20, 25, 27, 44, 53, 80]

target_value = 27
index = binary_search_rec(sortedL, target_value, 0, len(sortedL) - 1)

if index != -1:
    print(f"Found at index {index}")
else:
    print(f"Target not found")