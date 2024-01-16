def isPrime(n):
    if (n < 2):
        return False
    for factor in range(2,n):
        if (n % factor == 0):
            return False
    return True
#---------------------------------------
# And take it for a spin
for n in range(100):
    if isPrime(n):
        print(n, end=" ")
print()



def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2): # we start at 3 and step by 2 because we only need the odds
        if (n % factor == 0):
            return False
    return True


def nthPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (fasterIsPrime(guess)):
            found += 1
    return guess

# and let's see a list of the primes
for n in range(10):
    print(n, nthPrime(n))
print("Done!")