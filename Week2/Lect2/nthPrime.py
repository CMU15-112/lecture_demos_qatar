def isPrime(n):
    
    # reject not int
    if type(n) != int:
        return False
    
    # reject  < 2
    if n < 2:
        return False
    
    # special case
    if n == 2:
        return True
    
    #exclude even numbers
    if n%2 == 0:
        return False
    
    # reject if 2 -> sqrt(n) is a factor
    sqrtN = round(n**0.5)
    
    for i in range(2, sqrtN+1):
        if n%i == 0:
            return False
    
    return True


def nthPrime(n):
    count= 0
    val = 0
    while count < n:
         val += 1
         if isPrime(val):
             count+=1
    return val
             
    
    
    
print("isPrime")
for i in range(101):
    if isPrime(i) == True:
        print(i, " is Prime")
        
print("nthPrime")
for i in range(1,11):
    print(f"{i}th prime is {nthPrime(i)}")
    