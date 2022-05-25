"""
findDuplicates(L): 
Write the function hasDuplicates(L) that takes a 1d list L
of arbitrary values, and returns the list of duplicate values.
The order is not important, but there shouldn't be duplicate values
in the result
"""

# use L.count()



assert( findDuplicates([1,2,3]) == [])
assert( findDuplicates([1,1,1]) == [1])
assert( findDuplicates([1,4,2,1,3,4,5,1,2]) == [1,4,2])