"""
mySet = set()
mySet.add(5)
mySet.add(6)
mySet.add(7)
mySet.add(5)
mySet.add(10)
print(mySet)

if 5 in mySet:
    print("5 is there!")
"""

"""
import random

mySet = set()
myList = []

for i in range(1000000):
    num = random.randint(-1000000000,1000000000)
    mySet.add(num)
    myList.append(num)

print("Finished building set and list")    

print("Starting operations on the set...", end="")
found = 0
for i in range(100000000):
    if i in mySet:
        found += 1
print("done")
      
print("Starting operations on the list...", end="")
found = 0
for i in range(1000):
    if i in myList:
        found += 1
print("done")
        
print("I found", found, "items")
"""

myDictionary = dict()

myDictionary["Hi there"] = 6
myDictionary["Hi there"] = 32
myDictionary[32] = "Hey"
myDictionary[5.32] = 32

for i in myDictionary:
    print(i,":", myDictionary[i])

#print(myDictionary)
    