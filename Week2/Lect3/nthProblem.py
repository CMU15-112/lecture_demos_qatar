def is7ish(n):
    s = 0
    n = abs(n)
    while n > 0:
        s+= n%10
        n= n //10
    
    return (s%7==0)

def nth7ish(n):
    c =0
    v = 0
    while(c<n):
        v+=1
        if is7ish(v):
            c+=1
                  
    return v

assert(is7ish(16))      # True
assert(is7ish(25))      # True
assert(is7ish(18) == False)     # False

assert(nth7ish(0) ==0)     # 0
assert(nth7ish(1) == 7)     # 7
assert(nth7ish(2) == 14)     # 14
assert(nth7ish(3)  == 16)    # 16
assert(nth7ish(4) == 23)      # 23