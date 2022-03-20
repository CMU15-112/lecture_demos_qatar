# Write the recursive function interleave
# Now, what if len(list1) != len(list2)
# interleave([1,2,3], [4,5]) == [1,4,2,5,3]
# interleave([1], [4,5]) == [1,4,5]
# interleave([1,2,3], []) == [1,2,3]

# len(list1) = m
# len(list2) = n
# BigO using m, n = min(m, n)
def interleave(list1, list2):
    if list1 == []:
        return list2
    elif list2 == []:
        return list1
    else:
        res = interleave(list1[1:], list2[1:])
        return [list1[0], list2[0]] + res 

def interleaveIterative(list1, list2):
    n = len(list1)
    result = []
    for i in range(n):
        result.append(list1[i])
        result.append(list2[i])
    return result

