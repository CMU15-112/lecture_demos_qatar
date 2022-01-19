# print all numbers between 1 and n

def print1ToN(n):
    for i in range(n):    # from 0 to n-1
        print(i+1)
    
    


def print1ToNv2(n):
    for i in range(1,n+1,2):    # from 1 to n
        print(i)
        
print1ToNv2(10)