"""
in this version of the problem
we can assume n has at most 5 digits
"""
def sumDigits(n):
    sum = 0
    for i in range(5):
        sum += n%10
        n = n // 10
    return sum

def testSumDigits():
    print("Testing sumDigits... ")
    assert(sumDigits(112) == 4)
    assert(sumDigits(15112) == 10)
    assert(sumDigits(15112) == 10)

    print("passed")
testSumDigits()
