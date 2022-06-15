"""
Write the function recursiveSkipEveryNth(L, n) that takes a possibly-empty list of numbers, L,
and returns the list that results from skippng every nth value from L.
"""

assert(recursiveSkipEveryNth([1,2,3,4], 2) == [1,3])
assert(recursiveSkipEveryNth([1,2,3,4], 3) == [1,2,4])
assert(recursiveSkipEveryNth([1,2,3,4], 1) == [])


# the correct solution using a helper function
def recHelper(L, n, d):
    if len(L)==0:
        return []
    if d%n == 0:
        return recHelper(L[1:], n, d+1)
    else:
        return [L[0]] + recHelper(L[1:], n, d+1)

def recursiveSkipEveryNth(L, n):
    return recHelper(L, n, 1)
