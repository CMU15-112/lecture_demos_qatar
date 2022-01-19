# Find the sum of the digits of a non-negative number
def sumDigits(n):
    sumdigit = 0
    while n != 0:
        lastdigit = n%10  # take the last digit
        # remove it
        n = n // 10
        sumdigit = sumdigit + lastdigit
    return sumdigit
        


def testSumDigits():
    print("testing..")
    assert( sumDigits(15112) == 10)
    assert( sumDigits(15110) == 8)
    assert( sumDigits(15110) == 8)
    assert( sumDigits(0) == 0)
    assert( sumDigits(1) == 1)
    assert( sumDigits(99999) == 45)
    assert( sumDigits(1111111111) == 10)
    print("passed")

testSumDigits()
    