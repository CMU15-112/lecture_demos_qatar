def digitSum(n):
    theSum = 0
    while n > 0:
        digit = n % 10
        theSum += digit
        n //= 10
    return theSum

def doesSumTo(n, desiredSum):
    return digitSum(n) == desiredSum

def nthSumsTo(n, desiredSum): 
    found = 0
    guess = 0
    while found <= n:
        guess += 1
        if doesSumTo(guess, desiredSum):
            print(guess, found)
            found += 1
 
    return guess