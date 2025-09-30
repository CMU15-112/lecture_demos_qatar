# Write the function findDuplicates(L) that takes a list L of arbitrary values,
# and returns the list of duplicate values.
# The order is not important, but there shouldn't be duplicate values in the result

def findDuplicates(L):
    resL = []
    for e in L:
        if L.count(e) > 1:  # element is a dup
            if e not in resL:  # only keep one copy of the dup in res
                resL.append(e)
            print(f'{e} is a dup')
    
assert( findDuplicates([1,1,1,2]) == [1])
assert( findDuplicates([1,4,2,1,3,4,5,1,2]) == [1,4,2])
assert( findDuplicates([]) == [])
assert( findDuplicates([1,2,3]) == [])