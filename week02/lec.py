def f(n, m): #15, 10
    total = 0
    for x in range(n, m - 1, -1):
        if x % 2 == 1:
            total += x
    return total

print(f(15, 10))

print("---")


def printMystery(n):
    for row in range(n):
        print(row, end=" ")
        for col in range(row):
            print("*", end=" ")
        print()

printMystery(5)

print("---")


for i in range(10):
    if i == 2:
        continue
    print(i)
    
print("---")

for i in range(10):
    if i == 2:
        break
    print(i)
    
print("---")
result = 0
i = 10
while i < 21:
    result += i
    i += 1
print(result)
print(i)

print("---")
# Evenish: Positive integer where all digits are even
def isEvenish(n):
    if type(n) != int:
        return False
    if n <= 0:
        return False
    
    while n > 0:
        digit = n % 10
        
        if digit % 2 == 1:
            return False
        
        n = n // 10
    return True

print(isEvenish(12345))
print(isEvenish(8242))
print(isEvenish(8142))
print(isEvenish(-1234))
print(isEvenish(24.86))
print(isEvenish(24.76))

print("---")

# A positive integer with at least three digits and exactly 1 digit is odd
def isXOdd(n):
    if type(n) != int:
        return False
    #if n <= 0:
    #    return False
    if n < 100:
        return False
    
    oddCount = 0
    while n > 0:
        digit = n % 10
        
        if digit % 2 == 1:
            oddCount += 1   
            # Optimization
            if oddCount > 1:
                return False
            
        n //= 10
    
    return oddCount == 1

# Determine how many XOdd numbers there are > 0 and <= theMax
def countXOddNumbers(theMax):
    res = 0
    for i in range(0, theMax + 1):
        if isXOdd(i):
            res += 1
    return res

print(countXOddNumbers(102))

# Return the n'th XOdd number >= 0
# Example: nthXOddNumber(0) == 100
#          nthXOddNumber(1) == 102
#          nthXOddNumber(2) == 104
def nthXOddNumber(n):
    guess = -1 # Because the guess increment happens first, this needs to be -1
    seen = -1
    
    while seen != n:
        guess += 1
        if isXOdd(guess):
            seen += 1
    
    return guess

print(nthXOddNumber(0))
print(nthXOddNumber(1))
print(nthXOddNumber(2))
#print(nthXOddNumber(10000000))

# Given an integer n, what is the longest run of the number 42?
# Example:
# longest42run(12424256) == 2
# longest42run(12424256424242) == 3
def longest42run(n):
    n = abs(n)
    
    longestRun = 0
    cnt = 0
    while n != 0:
        # Do some stuff
        if n % 100 == 42:
            print("found a 42")
            cnt += 1
            if cnt > longestRun:
                longestRun = cnt
            n //= 100
        else:
            cnt = 0
            n //= 10
    return longestRun

print(longest42run(12424256424242))







































