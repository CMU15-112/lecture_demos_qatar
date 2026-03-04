'''
Write the function mostCommonName, that takes a list of names
(such as ["Jane", "Aaron", "Cindy", "Aaron"],
and returns the most common name in this list (in this case, "Aaron").

If there is more than one such name, return a set of the most common names.
So mostCommonName(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) returns the set
{"Aaron", "Jane"}. If the set is empty, return None.

Also, treat names case sensitively, so "Jane" and "JANE" are different names.
'''
def mostCommonName_n2(L):
    if len(L) == 0:
        return None
    
    maxCount = 0
    s = set()
    for e in L:   
        c = L.count(e)
        if c == maxCount:
            s.add(e)
        elif c > maxCount:
            s = {e}
            maxCount = c
    
    if len(s)== 1:
        return s.pop()
    
    return s

def mostCommonName_n(L):
    pass



def mostCommonName_nlogn(L):
    #Assume L = [D, C, A, B, D, B, D]
    pass



def testN2():
    print("Testing mostCommonName_n2()...", end="") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"}) 
    assert(mostCommonName_n2(["Cindy"]) == "Cindy") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"}) 
    assert(mostCommonName_n2([]) == None)
    print("Passed!")
    
    
def testNlogN():    
    print("Testing mostCommonName_nlogn()...", end="") 
    assert(mostCommonName_nlogn(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron") 
    assert(mostCommonName_nlogn(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"}) 
    assert(mostCommonName_nlogn(["Cindy"]) == "Cindy") 
    assert(mostCommonName_nlogn(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"}) 
    assert(mostCommonName_nlogn([]) == None)
    print("Passed!") 


def testN(): 
    print("Testing mostCommonName_n()...", end="") 
    assert(mostCommonName_n(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron") 
    assert(mostCommonName_n(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"}) 
    assert(mostCommonName_n(["Cindy"]) == "Cindy") 
    assert(mostCommonName_n(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"}) 
    assert(mostCommonName_n([]) == None)


def testMostCommonName():
    testN2()
#     testN()
#     testNlogN()

    print("Passed!")
    
testMostCommonName() 
