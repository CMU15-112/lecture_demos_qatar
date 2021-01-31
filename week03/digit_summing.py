def sumOfDigits(n):
    n = abs(n)
    theSum = 0
    while n > 0:
        digit = n % 10
        theSum += digit
        n //= 10
    return theSum

def digitsSumTo(n, desiredSum):
    return sumOfDigits(n) == desiredSum

# Return the nth number whose digits sum to
# desiredSum
def nthNumberWhoseDigitsSumTo(n, desiredSum):
    # Some sanity checking
    if isinstance(n, int) == False:
        return None
    if n < 1:
        return None
    
    numFound = 0
    guess = 0
    while numFound < n:
        if digitsSumTo(guess, desiredSum):
            numFound += 1
        guess += 1
        
    return guess-1

print(sumOfDigits(1234))
print(sumOfDigits(3442))
print(sumOfDigits(0))
print(sumOfDigits(2))
print(sumOfDigits(-5))
print("-----")
print(digitsSumTo(1234, 10))
print(digitsSumTo(1234, 9))
print("-----")
print(nthNumberWhoseDigitsSumTo(300, 12))