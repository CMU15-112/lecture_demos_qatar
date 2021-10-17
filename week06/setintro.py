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


# mySet.remove(10)
# print(mySet)
# 
# mySet.discard(8)
# print(mySet)
# 
# # Can you use sets to remove duplicates from a list?
# # Yes, but you lose the order
# myList = [5, 10, 15, 20, 10, 15, 17]
# print(myList)
# myTmpSet = set(myList)
# myList = list(myTmpSet)
# print(myList)
# 
# myList = [5, 10, 15, 20, 10, 15, 17]
# uniqItems = len(set(myList))
# 
# print("---")
# 
# mySet = {5,10,15,20}
# #newSet = {}
# newSet = set()
# print(type(mySet))
# print(type(newSet))
