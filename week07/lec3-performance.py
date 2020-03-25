import random

myList = []
mySet = set()

for i in range(10000):
    num = random.randint(-100000,100000)
    myList.append(num)
    
mySet = set(myList)

print("Searching the set....")
found = 0
for i in range(100001):
    if i in mySet:
        found += 1
print("I found ", found, "items")       

print("Searching the list...")
found = 0
for i in range(100001):
    if i in myList:
        found += 1       
print("I found ", found, "items")