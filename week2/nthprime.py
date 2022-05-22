# Returns the nth prime number (positive numbers)
# Note: The 0th prime number is 1.
#       The 1st prime number is 2.
#       The 2nd prime number is 3
#       The 3rd prime number is 5


# is we check 7
# 7%2, 7%3, 7%4, .., 7%6
# 2 up to 7-1
# 2 up to number -1

def isPrime(number):
    if number == 0:
        return False
    for factor in range(2, number):
        if number % factor == 0:
            return False
    return True 
    

def testIsPrime():
    print("Testing IsPrime...", end="")
    #print("isPrime(0) returns ", isPrime(0))
    assert( isPrime(0) == False )
    assert( isPrime(1) == True )
    assert( isPrime(2) == True )
    assert( isPrime(9) == False )
    assert( isPrime(11) == True )
    assert( isPrime(100) == False )
    assert( isPrime(101) == True )
    print("passed")

def nthPrime(n):
    numPrimesFound = 0
    guess = 0
    while numPrimesFound <= n:
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
  
#       The 0th prime number is 1.
#       The 1st prime number is 2=> when n=1, you should return 2, numPrimesFound = 2
#       The 2nd prime number is 3
#       The 3rd prime number is 5
    
# guess 1 -> numPrimesFound = 1
# guess 2 -> numPrimesFound = 2
# guess 3 -> numPrimesFound = 3
# guess 4 -> numPrimesFound = 3
# guess 5 -> numPrimesFound = 4

    

testIsPrime()
testNthPrime()

    
    