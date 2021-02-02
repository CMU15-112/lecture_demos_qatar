# Given a list of integers, calculate the alternating sum
# [1, 2, 3, 4] = 1 - 2 + 3 - 4 = -2
# 1 + -2 + 3 + -4
def alternatingSum(theList):
    theSum = 0
    for i in range(len(theList)):
        if i % 2 == 0:
            theSum += theList[i]
        else:
            theSum -= theList[i]
    return theSum

# result = alternatingSum([1,2,3,4])
# print(result)

def alternatingSumAgain(theList):
    positiveList = theList[0::2]
    negativeList = theList[1::2]
    return sum(positiveList) - sum(negativeList)

result = alternatingSumAgain([1,2,3,4])
print(result)