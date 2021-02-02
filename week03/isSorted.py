# Return True if the list of numbers is in sorted order
# Return False otherwise.
# [1, 2, 5, 7] -> True
# [1, 2, 5, 7, 6] -> False
def isSorted(theList):
    for i in range(len(theList)):
        if isinstance(theList[i], int) == False and isinstance(theList[i], float) == False:
            return False
    
    for i in range(len(theList)-1):
        if theList[i] > theList[i+1]:
            return False
    return True

print( isSorted([1,2,5,7]) )
print( isSorted([1,2,5.1,7]) )
print( isSorted([1,2,5,7,6]) )
print( isSorted([1,2,-5,5,7]) )
print( isSorted([1,2,2,7]) )
print( isSorted([]) )
print( isSorted([3]) )
print( isSorted([1,2,5.1,7]) )
print( isSorted([1,2,5.1,5.05]) )
print( isSorted([1,2,"Cat",5,7]) )
print( isSorted([1,2,True,5,7]) )
print( isSorted([1,2,3,5,None]) )