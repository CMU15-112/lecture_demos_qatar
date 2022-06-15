# Write the recursive function interleave
# Assume len(list1) == len(list2)
# Example: 
# interleave([1,2,3], [4,5,6]) == [1,4,2,5,3,6]
# interleave([1], [2]) == [1,2]
# interleave(['a','c'], ['b', 'd']) == ['a', 'b', 'c', 'd']

def interleave(A, B):
    if A==[] and B==[]::
        return []
    else:
        return [A[0], B[0] ] + interleave(A[1:], B[1:])
    