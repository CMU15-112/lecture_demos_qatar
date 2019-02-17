def slowIsPrime(n):
    if n < 2:
        return False
    
    for divisor in range(2,n):
        if n % divisor == 0:
            return False
    return True
    
def isPrime(n):
    if n == 2:
        return True
    elif n < 2 or n%2==0:
        return False
    
    maxValue = round(n**0.5)
    for divisor in range(2,maxValue+1):
        if n % divisor == 0:
            return False
    return True
    
# Return the nth prime
def nthPrime(n):
    foundPrimes = 0
    guess = 1
    while foundPrimes < n:
        guess += 1
        if isPrime(guess) == True:
            foundPrimes += 1
    return guess
        
    
# Perfect number is one where the sum of the divisors is itself
# Ex: 28

def stupidIsPerfectNumber(n):
    return True

def isPerfectNumber(n):
    sum = 0
    for divisor in range(1,n):
        if n%divisor == 0:
            sum += divisor
            
    if sum == n:
        return True
    else:
        return False
        

def nthPerfectNumber(n):
    foundNumbers = 0
    guess = 0
    while foundNumbers < n:
        guess += 1
        if isPerfectNumber(guess):
            foundNumbers += 1
    return guess
    
def testIsPerfectNumber():
    print("Testing isPerfectNumber...", end="")
    assert( isPerfectNumber(28) == True )
    assert( isPerfectNumber(30) == False )
    assert( isPerfectNumber(496) == True )
    assert( isPerfectNumber(6) == True )
    assert( isPerfectNumber(8128) == True )
    print("Passed!")
    
testIsPerfectNumber()
