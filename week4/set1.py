mySet = set()

mySet.add(5)
mySet.add(6)
mySet.add(10)
mySet.add(4)
mySet.add(5)

print(mySet)

for i in range(15):
    if i in mySet:
        print(i, " was in the set")

print("---")
