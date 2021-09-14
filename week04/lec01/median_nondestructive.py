"""
Write the non-destructive function median(a) that takes a list of floats and returns the median value,
which is the value of the middle element, or the average of the two middle elements.
If the list is empty, return None.
"""

def median(l):
    lcopy = l[:]
    lcopy.sort()
    if lcopy == []:
        return None
    
    if len(lcopy)%2==0:  # even
        return (lcopy[len(lcopy)//2] + lcopy[len(lcopy)//2-1])/2
    else:
        # do it yourself
        return 42
    
        
def verifyNondestructive():
    a = [1, 2, 3]
    b = a + []
    median(a)  # ignore result, just checking for destructiveness here
    return (a == b)

def testMedian():
    print("testing median() ...")
    assert( verifyNondestructive())
    assert( median([]) == None )
    assert( median([1]) == 1 )
    assert( median([1,2,3]) == 2 )
    assert( median([1,2,3,4]) == 2.5 )   # index 0,1,2,3 - I need index 1 and index 2,  len(l) = 4 4//2=2  4//2-1=1 - len(l)//2, len(2)//2-1
    assert( median([1,4]) == 2.5 )  
    assert( median([1.0,2.0,3.0,4.0]) == 2.5 )
    assert( median([40,2,3,1]) == 2.5 )
    
    print("all tests passed")
            
testMedian()



