import random

myList = []
mySet = set()

for i in range(100000):
    num = random.randint(-100000,100000)
    myList.append(num)
    mySet.add(num)

print(len(myList))
print(len(mySet))

print("Searching the set...")
found = 0
for i in range(0,100001):
    if i in mySet:
        found += 1
print("I found ", found, "items in the set")

print("Searching the list...")
found = 0
for i in range(0,100001):
    if i in myList:
        found += 1
print("I found ", found, "items in the list")