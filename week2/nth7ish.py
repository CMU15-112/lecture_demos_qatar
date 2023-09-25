def is7ish(n):  # Part 1
    sumdigit = 0
    n = abs(n)
    while n != 0:
        sumdigit += (n%10)
        n //= 10
    return sumdigit % 7 == 0    

def nth7ish(n): # Part 2
    found = 0
    guess = -1  			# Start with a guess that IS NOT a 7ish
    while (found != n+1):  	# we count from zero, so we need to find n+1 numbers
        guess += 1          # increment the guess first
        if (is7ish(guess)): # use the helper function (part 1) to check the guess
            found += 1      # increment the count
    return guess          	# IMPORTANT: you should understand why the last guess 
                            # is the answer
def badNth7ish(n):
    found = 0
    for i in range(10000000000000):
        if is7ish(i):
            found+=1
        if found == n+1:
            return i




print(badNth7ish(100))
print(badNth7ish(0))


