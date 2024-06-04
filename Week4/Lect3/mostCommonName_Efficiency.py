## Let's Modify what we did yesterday
def mostCommonName_n(L):
    if len(L) == 0:
        return None
    
    d= {}
    maxCount= 0
    maxElements= set()
    
    for e in L:
        d[e]= d.get(e, 0)+1
        
        if d[e] == maxCount:
            maxElements.add(e)
            
        elif d[e] > maxCount:
            maxElements= {e}
            maxCount= d[e]
            
    if len(maxElements) == 1:
        return maxElements.pop()
            
    return maxElements

def mostCommonName_n2(L):
    if len(L) == 0:
        return None
    
    #d= {}
    maxCount= 0
    maxElements= set()
    
    for e in L: # n iters
        c= L.count(e) #O(N)
        
        if c == maxCount:
            maxElements.add(e)
            
        elif c > maxCount:
            maxElements= {e}
            maxCount= c
            
    if len(maxElements) == 1:
        return maxElements.pop()
            
    return maxElements



def mostCommonName_nlogn(L):
    
    if len(L) == 0:
        return None
    
    L.sort()
    print(L)

    maxCount= 0
    maxElements= set()
    currCount= 1
    
    for i in range(len(L)-1):
        
        if L[i]==L[i+1]:
            currCount+=1
        else:
            e = L[i]
            if currCount == maxCount:
                maxElements.add(e)
                
            elif currCount > maxCount:
                maxElements= {e}
                maxCount= currCount
                
            currCount = 1
          
    print(maxElements)
    
    e= L[-1]
    if currCount == maxCount:
            maxElements.add(e)
                
    elif currCount > maxCount:
            maxElements= {e}
            maxCount= currCount
                
    if len(maxElements) == 1:
        return maxElements.pop()
            
    return maxElements



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
    testN()
    testN2()    
    testNlogN()

    print("Passed!")
    
testMostCommonName() 
