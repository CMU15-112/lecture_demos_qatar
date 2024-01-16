#while loops
n = 10
total = 0
while(n > 0):
    total+= n
    n-=1
print(total)



print("continue")

for i in range(10):
    if(i ==2):
        continue
    print(i)
    
    
print("break")
for i in range(10):
    if(i ==3):
        break
    
    print(i)