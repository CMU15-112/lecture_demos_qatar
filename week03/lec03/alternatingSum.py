# Given a list of integers, caculate the alternating sum
# [1, 2, 3, 4] = 1 - 2 + 3 - 4
# 1 + -2 + 3 + -4
def alternatingSum(theList):
    theSum = 0
    for i in range(len(theList)):
        if i % 2 == 0:
            theSum += theList[i]
        else:
            theSum += -theList[i]
    return theSum

def alternatingSumAgain(theList):
    theSum = 0
    posList = theList[0::2]
    negList = theList[1::2]
    return sum(posList) - sum(negList)

print(alternatingSum([1,2,3,4]))
print(alternatingSumAgain([1,2,3,4]))