def countDigit(n, d):
    cnt = 0
    while n != 0:
        digit = n %10
        if digit == d:
            cnt += 1
        n //= 10
    return cnt
    

# Return the digit that occurs most frequently in n
def mostFrequentDigit(n):
    mostSeenCount = 0
    mostSeenDigit = None
    
    for digit in range(10):
        count = countDigit(n, digit)
        if count >= mostSeenCount:
            mostSeenCount = count
            mostSeenDigit = digit
    return mostSeenDigit
        
n = 333444
print(mostFrequentDigit(n))