def isSpecial(n):
    # + int
    if type(n) != int:
        return False
    
    # 3 digits
    if n < 100 or n > 999:
        return False
    
    # multiple of 4 or 7
    return (n%4==0) or (n%7==0)

def nthSpecial(n):
    
    if n <=0 :
        return None
    
    count= 0
    number = 99
    
    while count < n:       
        number+=1
        if isSpecial(number):
            count+=1
            
    return number


for i in range(11):
    print(i, " ", nthSpecial(i))
    
            
        