def mostCommonName_n2(L):
    pass


def mostCommonName_n(L):
    pass


def mostCommonName_nlogn(L):
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
