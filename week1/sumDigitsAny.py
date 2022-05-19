# Write the function sumDigits that returns the sum of
# number digits (n is integer)
# n can have any number of digits
def sumDigits(n):   # assuming n
    n = abs(n)
    theSum = 0
    while n > 0:
        theDigit = n%10
        theSum = theSum + theDigit
        n = n // 10
    return theSum


assert(sumDigits(123) == 6)
assert(sumDigits(-123) == 6)
assert(sumDigits(1000) == 1)
assert(sumDigits(111111111111111) == 15)
assert(sumDigits(-1000) == 1)
assert(sumDigits(0) == 0)
assert(sumDigits(1) == 1)
print("it works!")
    
    