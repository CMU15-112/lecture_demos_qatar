# Return a reversed copy of the list
# For example:
# reverseList([1,2,3,4]) returns [4,3,2,1]
# This should be non-destructive
def reverseListNonDestructive(theList):
    retList = []
    for i in range(len(theList)-1, -1, -1):
        retList.append(theList[i])
    return retList

someList = [5, 10, 15, 20]
print(reverseListNonDestructive(someList))
print(someList)

print("---")

# Reverse a list in place.
# This should be destructive
def reverseListDestructive(theList):
    #theList = reverseListNonDestructive(theList) # Won't wory
    numItems = len(theList)
    for i in range(numItems):
        theList.insert(i, theList[-1])
        del theList[-1]
    return None

someList = [5,10,15,20]
print(reverseListDestructive(someList))
print(someList)