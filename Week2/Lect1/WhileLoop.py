count = 0
while count < 5:
    print(count)
    count+=1
print("Done")



print("------------------------")

def f1(n):
    n = abs(n)
    while(n >= 10):
        n= n//10
        
    return n

f1(72658)


print("------------------------")

def f2(n):
    r = 0
    while(n!=0):
        rem = n % 10
        r = r * 10 + rem
        n = n //10
    return r

print(f2(15112))