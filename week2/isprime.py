# return True if n is prime, false otherwise

def isPrime(n):
    if type(n) != int:
        return False
    if n <= 0:
        return False
    # we can catch the base cases 1 and 2
    if n == 1 or n == 2:
        return True

    # if it is even, we know it cannot be prime
    if n%2 == 0:
        return False

    # only check odd divisors
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    # here we know that it must be a prime number

    return True


def testIsPrime():
    print("Testing isPrime...", end="")
    assert( isPrime(2) == True)
    assert( isPrime(29) == True)
    assert( isPrime(7919) == True)
    assert( isPrime(4) == False)
    assert( isPrime(9) == False)
    assert( isPrime(5000) == False)
    assert( isPrime(-4) == False)
    assert( isPrime(3.45) == False)
    assert( isPrime("dog") == False)
    assert( isPrime(7.0) == False)
    print("done.")

testIsPrime()
