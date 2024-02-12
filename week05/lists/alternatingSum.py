# Given a list of integers, calculate the alternating sum...
# [1, 2, 3, 4] => 1 - 2 + 3 - 4 == 1 + -2 + 3 + -4

def alternatingSum(theList):
    sum = 0
    for i in range(len(theList)):
        if i % 2 == 0:
            sum += theList[i]
        else:
            sum -= theList[i]
    return sum

def otherAlternatingSum(theList):
    return sum(theList[::2]) - sum(theList[1::2])
    

def againAlternatingSum(theList):
    sum = 0
    for i in range(len(theList)):
        sum += (-1)**i * theList[i]
    return sum

print("Testing...", end="")
assert alternatingSum([1,2,3,4]) == -2
assert otherAlternatingSum([1,2,3,4]) == -2
assert againAlternatingSum([1,2,3,4]) == -2
print("passed")