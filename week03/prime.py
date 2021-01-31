# Returns True if n is prime and False otherwise
def isPrime(n):
    if isinstance(n, int) == False:
        return False
    
    if n < 2:
        return False
    
    for divisor in range(2, n):
        if n%divisor == 0:
            return False
    
    return True

def fasterIsPrime(n):
    if isinstance(n, int) == False:
        return False
    
    # Exclude negatives and 0,1
    if n < 2:
        return False

    # Exclude evens except 2
    if n != 2 and n%2 == 0:
        return False
    
    hi = int(n**0.5)+1
    for divisor in range(2, hi):
        if n%divisor == 0:
            return False
    
    return True

# for i in range(50):
#     print(i, isPrime(i))
# print(isPrime(2.5))
# print(isPrime("Cat"))

# Returns the nth prime number
def nthPrime(n):
    # Some sanity checking
    if isinstance(n, int) == False:
        return None
    if n < 1:
        return None

    numPrimesFound = 0
    guess = 2
    while numPrimesFound < n:
        if fasterIsPrime(guess):
            numPrimesFound += 1
        guess += 1
    
    return guess-1

for i in range(1,50):
    print(i, nthPrime(i))
print(nthPrime(0))