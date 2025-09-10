""" using a while loop """
def sumDigits(n):
    theSum = 0
    while n > 0:
        theSum += n%10
        n = n // 10
    return theSum

            

def testSumDigits():
    print("Testing sumDigits... ")
    assert(sumDigits(112) == 4)
    assert(sumDigits(1511215112) == 20)
    assert(sumDigits(42) == 6)
    #assert(sumDigits(-42) == 6)  # add later,
                                  # what do you need to change to
                                  # consider this test?
    print("passed")
    
testSumDigits()