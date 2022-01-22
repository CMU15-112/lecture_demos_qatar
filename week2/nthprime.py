def isPrime(n):
    if type(n) != int:
        return False
    if n <= 0:
        return False
    if n == 1 or n == 2:
        return True
    if n%2 == 0:
        return False   
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True

# Returns the nth prime number
# Note: The 0th prime number is 1.
#       The 1st prime number is 2.
def nthPrime(n):
    numPrimesFound = 0
    guess = 0
    while numPrimesFound < n+1:  # when numPrimesFound == n+1 this will be false, and the while ends
        guess += 1
        if isPrime(guess):
            numPrimesFound += 1
    return guess

def testNthPrime():
    print("Testing NthPrime...", end="")
    assert( nthPrime(0) == 1 )
    assert( nthPrime(1) == 2 )
    assert( nthPrime(2) == 3 )
    assert( nthPrime(3) == 5 )
    assert( nthPrime(4) == 7 )
    assert( nthPrime(5) == 11 )
    print("passed")
    
testNthPrime()