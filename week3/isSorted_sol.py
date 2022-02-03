# return True if theList is sorted
def isSorted(theList):
    for i in range(len(theList)):
        if isinstance(theList[i], int) == False and isinstance(theList[i], float) == False:
            return False
    
    for i in range(len(theList)-1):
        if theList[i] > theList[i+1]:
            return False
    return True

def isSortedv2(theList):
    for i in range(len(theList)):
        if isinstance(theList[i], int) == False and isinstance(theList[i], float) == False:
            return False
    return theList == sorted(theList)
    

