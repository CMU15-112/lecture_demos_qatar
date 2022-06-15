# a function that sums the digits of an integer, recursively!


# bottom-up: the work is done on the "way up"
def sumList(l):
    if l == []:
        return 0
    else:
        return l[0] + sumList(l[1:])

# top-down: the work is done on the "way down"
def sumList(l, sumsofar=0):
    if l == []:
        return sumsofar
    sumsofar += l[0]
    return sumList(l[1:], sumsofar)


"""
sumList([5,3,2,6]) -> sumList([5,3,2,6], 0) -> 16
sumList([3,2,6], 5) -> 16
sumList([2,6], 8) -> 16
sumList([6], 10) -> 16
sumList([], 16) -> 16
"""
assert(sumList([5,3,2,6]) == 16)
assert(sumList([]) == 0)
assert(sumList([2, -2]) == 0)
print("passed")
