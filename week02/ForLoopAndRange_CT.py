n=15
m=10

total = 0
for x in range(n, m-1, -1):
    if (x % 2 == 1):
        total += x
        
print(total)