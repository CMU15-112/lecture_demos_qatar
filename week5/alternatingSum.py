# Given a list of positive integers, calculate the alternating sum
# alternatingSum([1, 2, 3, 4]) == -2  because 1 - 2 + 3 - 4 = -2
# alternatingSum([15, 5, 10, 1]) == -2  because 15 - 5 + 10 - 1 = 19

def alternatingSum(L):
    return sum(L[::2]) - sum(L[1::2])

assert alternatingSum([15, 5, 10, 1]) == 19
assert alternatingSum([1, 2, 3, 4]) == -2
assert alternatingSum([1, 0, 1, 0]) == 2
assert alternatingSum([0, 1, 0, 1]) == -2
print(":-)")