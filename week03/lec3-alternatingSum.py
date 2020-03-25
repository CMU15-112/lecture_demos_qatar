# Given a list of integers, calculate the alternating sum
# Example:
# [1,2,3,4] becomes 1 - 2 + 3 - 4 = -2
def alternatingSum(theList):
    positiveNumbers = theList[0:len(theList):2]
    negativeNumbers = theList[1:len(theList):2]
    return sum(positiveNumbers) - sum(negativeNumbers)

def otherAlternatingSum(theList):
    sum = 0
    for i in range(len(theList)):
        if i % 2 == 0:
            sum += theList[i]
        else:
            sum -= theList[i]
    return sum

print(otherAlternatingSum([1,2,3,4]))