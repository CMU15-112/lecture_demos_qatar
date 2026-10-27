def sumDigits(n):
    if n < 10:
        return n
    else:
        lastDigit = n % 10
        result = lastDigit + sumDigits(n//10)
        return result
    
print(sumDigits(123))