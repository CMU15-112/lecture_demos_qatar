# Write the recursive function interleave
# Assume len(list1) == len(list2)
# Example: 
# interleave([1,2,3], [4,5,6]) == [1,4,2,5,3,6]
# interleave([1], [2]) == [1,2]
# interleave(['a','c'], ['b', 'd']) == ['a', 'b', 'c', 'd']
# interleave([], []) == []

def interleave(list1, list2):
    if list1==[] and list2==[]:
        return []
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