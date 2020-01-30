# Return true if all the elements of someList are in order
# Note: You are not allowed to sort the list
# Sample:
# [1, 2, 5, 8, 7]
#
def isSorted(someList):
    for i in range(len(someList)-1):
        if someList[i] > someList[i+1]:
            return False
    return True

print(isSorted([1,2,3,4]))
print(isSorted([1]))