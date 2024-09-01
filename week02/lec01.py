import sys

for i in range(0, 10):
    print(i, "Hi")
    
# Sum all the numbers from 10 to 20 (inclusive)
res = 0
for i in range(10, 21):
    res += i
print("Sum is ", res)

# Sum all the even numbers from 20 to 100 (not inclusive)
res = 0
for i in range(20, 100):
    if i % 2 == 0:
        res += i
print("Sum is ", res)

res = 0
for i in range(20, 100, 2):
    res += i
print("Sum is ", res)

# Sum numbers, but backwards
res = 0
for i in range(20, 9, -1):
    #print(i)
    res += i
print("Sum is ", res)

# Nested loops
#for i in range(5):
#    for j in range(10):
#        print("i = ", i, "j = ", j)

# Continue
for i in range(10):
    if i == 2:
        continue
    print(i)
    
# Break
for i in range(10):
    if i == 3:
        break
    print(i)
print("done")

# While loops

result = 0
i = 10
while i < 21:
    result += i
    i += 1
print(result)