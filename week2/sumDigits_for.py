# Find the sum of the digits of a non-negative number, assuming we have up to 5 digits
# If we assume that n can have up to 5 digits, we can use a for-loop
def sumDigits(n):
    sumdigit = 0
    for i in range(5):
        print("value of n before iteration ",i, "=", n)
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
    assert( sumDigits(99) == 18)
    assert( sumDigits(99999) == 45)
    print("passed")

testSumDigits()
