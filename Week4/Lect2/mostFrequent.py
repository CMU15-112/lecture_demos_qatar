def mostFrequent(L):
    # Return most frequent element in L, 
        #resolving ties arbitrarily.
    d= {}
    maxCount= 0
    maxE= None
    
    for e in L:
        d[e]= d.get(e, 0)+1
        
        if d[e] > maxCount:
            maxE= e
            maxCount= d[e]
            
    return maxE
  
    
    

def testMostFrequent():
    print("Testing mostFrequent()... ", end="")
    assert(mostFrequent([2,5,3,4,6,4,2,4,5]) == 4)
    assert(mostFrequent([2,3,4,3,5,3,6,3,7]) == 3)
    assert(mostFrequent([42]) == 42)
    assert(mostFrequent([]) == None)
    print("Passed!")

testMostFrequent()