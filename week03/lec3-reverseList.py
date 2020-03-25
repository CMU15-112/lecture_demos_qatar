# Non-destructive
def myReverseListNonDestructive(myList):
    retList = []
    for i in range(len(myList)-1,-1,-1):
        retList.append(myList[i])
    return retList

def myReverseListAgain(myList):
    retList = []
    for i in range(len(myList)):
        retList.append(myList[len(myList)-i-1])
    return retList

def myReverseListDestructive(myList):
    lengthOfInput = len(myList)
    for i in range(lengthOfInput):
        myList.insert(i, myList[-1])
        del myList[-1]
    return None
        
def myReverseListDestructiveAgain(myList):
    retList = []
    for i in range(len(myList)-1,-1,-1):
        retList.append(myList[i])
    
    del myList[:]
    for i in range(len(retList)):
        myList.append(retList[i])
    

someList = [5, 10, 15, 20]
newList = myReverseListNonDestructive(someList)

print(newList)
print(someList)

myReverseListDestructive(someList)
print(someList)