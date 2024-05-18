def isPrime(n):
    
    if n < 2:
        return False
    
    for i in range(2, n):
        if n%i ==0:
            return False
        
    return True
        

def betterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2): # we start at 3 and step by 2 because we only need the odds
        if (n % factor == 0):
            return False
    return True

def nthPrime(n):   
    
    number = 1
    count= 0
    
    while count < n:     
        number+=1       
        if isPrime(number):
            count+=1
  
    return number

print("nth Prime")
for i in range(1, 10):
    print(nthPrime(i))
        