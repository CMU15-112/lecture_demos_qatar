# Longest 42 run

def longest42Run(n):

    longestRun = 0
    count = 0
    while n > 0:
        tmp = n % 100
        #print("Checking:", tmp)
        if tmp == 42:
            count += 1
            if count > longestRun:
                #print("Found a longer run!")
                longestRun = count
            #print("Found a 42.  Count is ", count)
            n //= 100
        else:
            count = 0
            n //= 10
    return longestRun

def testLongest42Run():
    print("Testing...", end="")
    assert longest42Run(424200) == 2
    assert longest42Run(42) == 1
    assert longest42Run(424) == 1
    assert longest42Run(421142) == 1
    assert longest42Run(15112) == 0
    assert longest42Run(142424242424200) == 6
    assert longest42Run(142424242004242) == 4
    assert longest42Run(424214242424200) == 4
    print("done")
    
testLongest42Run()

