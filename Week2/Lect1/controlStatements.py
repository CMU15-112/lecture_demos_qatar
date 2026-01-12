
#### Continue
for i in range(5):
    if i == 2:
        continue
    print(i)
    
total = 0
for i in range(11):
    if (i%2) == 1:
        continue
    total+=i
    
print(total)

print("--------- Break")

#### Break
for i in range(5):
    if i == 3:
        break
    print(i)