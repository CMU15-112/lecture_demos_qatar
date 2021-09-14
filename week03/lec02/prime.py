# Determine if n is prime.
# Returns true or false
# n should be positive and an integer
# Don't use a float.  You might think that is ok,
# but you are wrong.
def isPrime(n):
    if isinstance(n,int) == False or n < 0:
        return False
    
    for divisor in range(2,n):
        if n%divisor == 0:
            return False
    return True

# Returns the nth prime number
# Note: The 0th prime number is 1.
#       The 1st prime number is 2.
def nthPrime(n):
    
    numPrimesFound = 0
    guess = 0
    while numPrimesFound <= n:
        guess += 1
        if isPrime(guess):
            numPrimesFound += 1
 
    return guess

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
    
def testNthPrime():
    print("Testing NthPrime...", end="")
    assert( nthPrime(0) == 1 )
    assert( nthPrime(1) == 2 )
    assert( nthPrime(2) == 3 )
    assert( nthPrime(3) == 5 )
    assert( nthPrime(4) == 7 )
    assert( nthPrime(5) == 11 )
    print("done.")
    
testNthPrime()