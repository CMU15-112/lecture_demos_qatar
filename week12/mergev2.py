def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    return merge(leftHalf, rightHalf)

def merge(left, right):
    result = []
    i = 0  # pointer for left list
    j = 0  # pointer for right list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

L = [38, 27, 43, 3, 9, 82, 10]
sortedL = mergeSort(L)
print(f"Original list: {L}")
print(f"Sorted list: {sortedL}")