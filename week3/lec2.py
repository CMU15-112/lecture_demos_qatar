# Sum all the digits in positive integer n
def digitSummer(n):
    sum = 0
    while n > 0:
        d = n % 10
        sum += d
        n //= 10
    return sum

def doDigitsSumTo(theNumber, desiredSum):
    return digitSummer(theNumber) == desiredSum
    
assert(doDigitsSumTo(123,6) == True)
assert(doDigitsSumTo(123,7) == False)
assert(doDigitsSumTo(100003498,25) == True)

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

def nthNumberDigitsSumTo(n, desiredSum):
    numFound = 0
    guess = 0
    
    while numFound < n:
        guess += 1
        if doDigitsSumTo(guess,desiredSum):
            numFound += 1
            
    return guess

print(nthNumberDigitsSumTo(10000,6))
