def longest42run(n):
    
    curr42SeqLen=0
    longestSeq=0
    
    while(n>0):
        
        if n%100 == 42:
            curr42SeqLen+=1
            longestSeq= max(curr42SeqLen, longestSeq)
            n= n//100
        else:
            curr42SeqLen= 0
            n= n//10
            
    return longestSeq


def testLongest42Run():
    assert(longest42run(424200) == 2)
    assert(longest42run(42) == 1)
    assert(longest42run(424) == 1)
    assert(longest42run(421142) == 1)
    assert(longest42run(15112) == 0)
    assert(longest42run(142424242424200) == 6)
    assert(longest42run(142424242004242) == 4)
    
    print("PASSED !!")
    
testLongest42Run()