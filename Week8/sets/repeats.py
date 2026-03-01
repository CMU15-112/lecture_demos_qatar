'''
Write a function repeats(L) which takes as an input a list (L)
and returns a sorted list of repeated elements in the list L.
    
    assert(repeats([1,2,3,2,1]) == [1,2])
    assert(repeats([1,2,3,2,2,4]) == [2])
    assert(repeats(list(range(100))) == [ ])
    assert(repeats(list(range(100))*5) == list(range(100)))
'''

def repeats(L):
    # return a sorted list of the repeat elements in the list L
    pass

def testRepeats():
    print("Testing repeats()...", end="")
    assert(repeats([1,2,3,2,1]) == [1,2])
    assert(repeats([1,2,3,2,2,4]) == [2])
    assert(repeats(list(range(100))) == [ ])
    assert(repeats(list(range(100))*5) == list(range(100)))
    print("Passed!")

testRepeats()
  
    
    
    
    
    
    
    
