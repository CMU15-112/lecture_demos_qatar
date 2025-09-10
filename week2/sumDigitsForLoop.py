import math

""" sumDigits using getKthDigit and a for loop """
def digitCount(n):
    n = abs(n)
    if n == 0:
        return 1
    return 1 + math.floor(math.log10(n))

def getKthDigit(n, k):
    n = abs(n)
    return (n // 10**k) % 10

def sumDigits(n):
    ndigits = digitCount(n)
    theSum = 0
    for i in range(ndigits):
        d = getKthDigit(n, i)
        theSum += d
    return theSum

    
def testSumDigits():
    print("Testing sumDigits... ")
    assert sumDigits(112) == 4
    assert sumDigits(1511215112) == 20
    assert sumDigits(42) == 6
    # it also handles negative cases, why?
    assert sumDigits(-42) == 6
    print("all tests passed")
    
testSumDigits()