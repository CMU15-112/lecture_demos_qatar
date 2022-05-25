# n is an int
# n must be in the interval [100, 999]
# n = ba
# b has 2 digits
# b is a perfect square:
# b can be 16, 25, 36, 49, 64, 81
# b = a*a
# b = 36
# a = 6
# n = 366
import math
def rc1(n):
    if ((not isinstance(n, int)) or (n < 100) or (n > 999)):
        return False
    a = n % 10
    b = n // 10
    return (math.isclose(b**0.5, a) and (a + b ==  42))

print(rc1(366))