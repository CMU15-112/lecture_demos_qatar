def is7ish(n):
    sumdigit = 0
    n = abs(n)
    while n != 0:
        sumdigit += (n%10)
        n //= 10
    return sumdigit % 7 == 0    

def nth7ish(n):
    found = 0
    guess = -1
    while (found <= n):
        guess += 1
        if (is7ish(guess)):
            print(guess)
            found += 1
    return guess

print(nth7ish(1))
