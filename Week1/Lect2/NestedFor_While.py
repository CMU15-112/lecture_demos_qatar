for x in range(3):
    for y in range(3):
        print("(", x, ", ", y, ") ", end= " ")
    print()
    

n =0
while(n <3):
    print(n)
    n+=1
    
def f(n):
    n = abs(n)
    while(n >= 10):
        n= n//10
        
    return n

f(12345)