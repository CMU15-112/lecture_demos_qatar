
def getAverage():
    c = 0
    s = 0
    v = int(input("Enter value (-1 to stop)"))
    while v != -1:
        c = c + 1
        s = s + v
        v = int(input("Enter value (-1 to stop)"))
    if c != 0:
        return s/c
    else:
        return 0
def isPrime(n):
    for i in range(2,int(ceil(n**0.5))):
        if n % i == 0:
            return False
    return True

def findnthPrime(n):
    number = 2
    count = 0
    while count != n:
        if isPrime(number):
            count += 1
        number += 1
    return number - 1
print (findnthPrime(351))
print (getAverage())


