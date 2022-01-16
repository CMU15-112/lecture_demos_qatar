def getOnesDigit(n):
    return n%10

# use assert to test your functions
assert( getOnesDigit(15112) == 2)
assert( getOnesDigit(15111) == 1)
assert( getOnesDigit(15123) == 3)


def testGetOnesDigit():
    print("Testing getOnesDigit...", end="")
    assert( getOnesDigit(123) == 3)
    assert( getOnesDigit(4237) == 7)
    assert( getOnesDigit(0) == 0)
    assert( getOnesDigit(2) == 2)
    assert( getOnesDigit(2.3) == 2)
    assert( getOnesDigit(-123) == 3)
    print("done.")
