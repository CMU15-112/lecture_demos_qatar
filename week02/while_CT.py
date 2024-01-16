def f(n): #leftmostDigit
    n = abs(n)
    while (n >= 10):
        n = n//10
        
    return n

print(f(72658489290098))