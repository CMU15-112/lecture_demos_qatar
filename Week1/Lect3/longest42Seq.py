def longest42run(n):
    
    currSeqLen= 0
    maxSeqLen= 0
    
    while n >0:
        if n%100 == 42:
            currSeqLen+=1
            maxSeqLen= max(currSeqLen, maxSeqLen)
            n= n//100
        else:
            currSeqLen = 0
            n= n//10
        
    return maxSeqLen



def testLongest42Run():
    assert(longest42run(424200) == 2)
    assert(longest42run(42) == 1)
    assert(longest42run(421142) == 1)
    assert(longest42run(15112) == 0)
    assert(longest42run(14242342424287421) == 3)
    assert(longest42run(142424242424200) == 6)
    assert(longest42run(142424242004242) == 4)
    print("Passed !!!")
    
testLongest42Run()