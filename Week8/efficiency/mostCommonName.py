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
    for e in L:  # N 
        c = L.count(e) # N
        if c == maxCount:
            s.add(e)
        elif c > maxCount:
            s = {e}
            maxCount = c
    
    if len(s)== 1:
        return s.pop()
    
    return s

def mostCommonName_n(L):
    if len(L) == 0:
        return None
    
    d = {}
    maxCount = 0
    s = set()
    #L = [D, C, A, B, D, B, D]
    #d = {D:3, C:1, A:1, B:2 }
    #s = {D}
    for e in L:  # N
        d[e] = d.get(e, 0)+1 # O(1)
        c = d[e]
        if c == maxCount:
            s.add(e)
        elif c > maxCount:
            s = {e}
            maxCount = c
    
    if len(s)== 1:
        return s.pop()
    
    return s
    

def mostCommonName_nlogn(L):
    #Assume L = ['D', 'C', 'A', 'B', 'D', 'B', 'D']
    if len(L) == 0:
        return None
    
    L.sort() #
    # sl = ['A','B','B','C','D','D','D']
    #print(L)
    
    currCount = 1
    maxCount = 0
    maxElements = set()
    
    # for i in range(1, len(L)): #len(L)-1
        # L[i] == L[i-1]
        
    for i in range(len(L)-1): # len(L)-2
        if L[i] == L[i+1]:
            currCount+=1
        else: # new item
            e = L[i]
            if currCount == maxCount:
                maxElements.add(e)
            elif currCount > maxCount:
                maxElements= {e}
                maxCount = currCount
            currCount= 1
    
    e = L[-1]
    if currCount == maxCount:
        maxElements.add(e)
    elif currCount > maxCount:
        maxElements= {e}
        maxCount = currCount
    
    if len(maxElements)== 1:
        return maxElements.pop()
    
    print(maxElements)
    return maxElements



def testN2():
    print("Testing mostCommonName_n2()...", end="") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron")
    # ...["Aaron", "Aaron", "Cindy", "Jane", "Jane"]
    assert(mostCommonName_n2(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]) == {"Aaron", "Jane"}) 
    assert(mostCommonName_n2(["Cindy"]) == "Cindy") 
    assert(mostCommonName_n2(["Jane", "Aaron", "Cindy"]) == {"Aaron", "Cindy", "Jane"}) 
    assert(mostCommonName_n2([]) == None)
    print("Passed!")
    
    
def testNlogN():    
    print("Testing mostCommonName_nlogn()...", end="") 
    assert(mostCommonName_nlogn(["Jane", "Aaron", "Cindy", "Aaron"]) == "Aaron")
    print("Testing")
    print(mostCommonName_nlogn(["Jane", "Aaron", "Jane", "Cindy", "Aaron"]))
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
    testN()
    testNlogN()

    print("Passed!")
    
testMostCommonName() 
