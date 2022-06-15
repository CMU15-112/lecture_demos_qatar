"""
Write the function recursiveSkipEveryNth(L, n) that takes a possibly-empty list of numbers, L,
and returns the list that results from skippng every nth value from L.

assert(recursiveSkipEveryNth([1,2,3,4], 2) == [1,3])
assert(recursiveSkipEveryNth([1,2,3,4], 3) == [1,2,4])
assert(recursiveSkipEveryNth([1,2,3,4], 1) == [])
"""


def recursiveSkipEveryNth(L, n, indexsofar=0):
    if L==[]:
        return []
    # L[0] <-> L[i]
    if (indexsofar+1)%n==0:
        return recursiveSkipEveryNth(L[1:], n, indexsofar+1)
    else:
     return [L[0]] + recursiveSkipEveryNth(L[1:], n, indexsofar+1)

# solving iteratively can help to understand how to solve the problem recursively
def IterativeSkipEveryNth(L, n):
    res = []
    for i in range(len(L)):
        if (i+1)%n==0:
            continue
        res.append(L[i])
    return res

assert(IterativeSkipEveryNth([1,2,3,4], 2) == [1,3])
assert(IterativeSkipEveryNth([1,2,3,4], 3) == [1,2,4])
assert(IterativeSkipEveryNth([1,2,3,4], 1) == [])
print("passed")
