# Determine if n is prime.
# Returns true or false
# n should be positive and an integer
def isPrime(n):
    if n < 0:
        return False
    
    for divisor in range(2,n):
        if n%divisor == 0:
            return False
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
    print("done.")
    
testIsPrime()
  
    