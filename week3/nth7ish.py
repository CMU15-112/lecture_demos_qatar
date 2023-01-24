# a 7ish number is a positive integer s.t.
# the sum of its digits is multiple of 7
# find the nth 7ish number
# nth7ish(0) =


def is7ish(n):
    sumdigit = 0
    while n > 0:
        sumdigit += (n%10)
        n //=10
    return (sumdigit % 7) == 0
    
    
def nth7ish(n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (is7ish(guess)):
            found += 1
    return guess
    
    
    