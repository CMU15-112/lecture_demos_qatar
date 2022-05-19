# Write the function sumDigits that returns the sum of
# number digits (n is integer)
# Assume that the number can have up to 5 digits

# 1. convert the number to positive
# 2. extract all digits, store them in variables
# 3. compute the sum
# 4. return the sum


# try with n=-123
# -123 -> 123
# v1 = 3
# v10 = 2
# v100 = 1
# v1000 = 0
# sum v1+v2+v3 = 6
# return 6

# try with n =1000
# 1000
# v1 = 0
# v10 = 0
# v100 = 0
# v1000 = 1
# sum = 1

def sumDigits1(n):   # assuming n
    n = abs(n)
    v1 = n%10
    n = n // 10
    v10 = n %10
    n = n // 10
    v100 = n % 10
    n = n // 10
    v1000 = n % 10
    n = n // 10
    v10000 = n % 10
    return v1 + v10 + v100 + v1000 + v10000

def sumDigits(n):   # assuming n
    n = abs(n)
    theSum = 0
    for i in range(5):
        theDigit = n%10
        theSum = theSum + theDigit
        n = n // 10
    return theSum
    
    

assert(sumDigits(123) == 6)
assert(sumDigits(-123) == 6)
assert(sumDigits(1000) == 1)
assert(sumDigits(-1000) == 1)
assert(sumDigits(0) == 0)
assert(sumDigits(1) == 1)
print("it works!")


    
    

    