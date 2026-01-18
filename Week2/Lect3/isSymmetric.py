
def numDigits(n):
    
    if n ==0:
        return 1
    
    c = 0
    while n > 0:
        n = n//10
        c+=1
    return c    
    

def isSymmetricNumber(n):
    
    if type(n) != int or n < 0:
        return False
    
    x = numDigits(n)
    
    if x %2 != 0:
        return False
    
    power = 10**(x/2)
    part1 = n // power
    part2 = n% power
    
    return part1 == part2


print(isSymmetricNumber(99)        )         # True
isSymmetricNumber(2020)               # True
isSymmetricNumber(4554)               # False
isSymmetricNumber(789987)             # False
isSymmetricNumber(444555666444555666) # True
isSymmetricNumber(0)                  # False (odd number of digits)
print(isSymmetricNumber(-2020)   )           # False