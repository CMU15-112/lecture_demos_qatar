#mySet = set()

mySet= {1, 4, 3, 6, 7}

mySet.add(5)
mySet.add(6)
mySet.add(10)
mySet.add(4)
mySet.add(5)

print(mySet)

#print(mySet[1])  # not possible!!!

for e in mySet:
    print(f"Elem {e} is in the set")

#mySet.remove(20)

for i in range(15):
    if i in mySet:
        print(i, " was in the set")

print("---")