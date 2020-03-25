def loopTest():
    for i in range(5):
        print(i)
        
def loopTest2():
    for i in [0, 2, 6, 10, 3]:
        print(i)
        
def loopTest3():
    for i in range(0,10,2):
        print(i)

def printAllOddNumbers(m, n):
    for i in range(m, n+1):
        if i % 2 != 0:
            print(i)

def printAllOddNumbersAnotherWay(m,n):
    if m % 2 == 0:
        m += 1
    # Works if... m is odd
    for i in range(m,n+1,2):
        print(i)

def whileLoopDemo():
    n = 0
    while(n < 10):
        print(n)
        n += 2

# Return True if n is prime, False otherwise
def isPrime(n):
    if type(n) != int:
        return False
    
    if n < 2:
        return False
    
    for divisor in range(2, n):
        if n%divisor == 0:
            return False

    return True

def fasterIsPrime(n):
    if type(n) != int:
        return False
    
    if n < 2:
        return False
    
    if n!=2 and n%2==0:
        return False
    
    hi = int(n**0.5)+1
    for divisor in range(3, hi):
        if n%divisor == 0:
            return False

    return True    

# Return the nth prime number.
# The first prime number is 2
def nthPrime(n):
    numFoundPrimes = 0
    
    guess = 1
    while numFoundPrimes < n:
        guess += 1
        if isPrime(guess):
            numFoundPrimes += 1
        

    return guess