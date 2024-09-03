# Return true if a number is evenish and false otherwise.
# Evenish means all the digits are even.
# 246
# 124
# 0
def isEvenish(n):
    n = abs(n)
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            return False
        n //= 10
    return True

# Is Exclusively Odd - The number is at least 3 digits and has exactly 1 odd digit.
def isXOdd(n):
    n = abs(n)
    
    if n < 100:
        return False

    count = 0
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            count += 1
        n //= 10
    return count == 1

# EvenishCount - Determine how many numbers >= 0 and less than elem are evenish
def evenishCount(elem):
    count = 0
    for i in range(elem):
        if isEvenish(i):
            count += 1
    return count

# Determine the nth evenish number.
# for n=0, the answer is 0
# for n=1, the answer is 2
def nthEvenish(n):
    count = 0
    num = -1
    
    n = n + 1
    
    while n != count:
        num += 1
        if isEvenish(num):
            count += 1
            
    return num