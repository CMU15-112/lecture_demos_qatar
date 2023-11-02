# Sets cannot contain repeated elements
# and will silently ignore any attempt to 
# add duplicates

mySet = set()

mySet.add(5)
mySet.add(6)
mySet.add(10)
mySet.add(4)
mySet.add(5)

print(mySet)
