# Write the recursive function interleave
# Example: 
# interleave([1,2,3], [4,5,6]) == [1,4,2,5,3,6]
# interleave([1], [2]) == [1,2]
# interleave(['a','c'], ['b', 'd']) == ['a', 'b', 'c', 'd']
# interleave([1,2,3], [4,5]) == [1,4,2,5,3]
# interleave([1], [4,5]) == [1,4,5]
# interleave([1,2,3], []) == [1,2,3]

def interleave(A, B):
    if A==[] or B==[]:
        return A+B
    else:
        return [A[0], B[0] ] + interleave(A[1:], B[1:])
    
def interleave(A, B):
    if A==[]:
        return B
    elif B==[]:
        return A
    else:
        return [A[0], B[0] ] + interleave(A[1:], B[1:])
    
assert(interleave([1,2,3], [4,5]) == [1,4,2,5,3])
assert(interleave([1], [4,5]) == [1,4,5])
assert(interleave([1,2,3], []) == [1,2,3])