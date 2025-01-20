"""
In this version of the problem, n can have any length
"""
def sumDigits(n):
    n =abs(n)
    sum =0
    while n!=0:
        sum += n%10
        n = n //10
    return sum



def testSumDigits():
    print("Testing sumDigits... ")
    assert(sumDigits(112) == 4)
    assert(sumDigits(15112) == 10)
    assert(sumDigits(15112) == 10)
    assert(sumDigits(-15112) == 10)

    print("passed")
testSumDigits()
