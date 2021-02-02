myList = [10, 20, 14, 8, 3, 2, 89, -100]
print(myList)
print(myList[4])
print(myList[1])
print(myList[0])
print(type(myList))
print(type(myList[0]))
print(myList[-1])
print(myList[-2])

print("----")
x = myList[0] + 8
print(x)

print("----")
for i in range(len(myList)):
    print(myList[i])

print("----")
myList[0] = 100
print(myList)
myList[1] += 1
print(myList)

print("----")
for i in range(len(myList)):
    myList[i] += 5
print(myList)

# myList[8] = 76
myList.append(76)
print(myList)
myList.insert(2,87)
print(myList)

print("----")
newList = myList[0:5]
print(newList)
print(myList)

newList2 = myList[2:7]
print(newList2)

newList3 = myList[:7]
print(newList3)

newList4 = myList[6:]
print(newList4)

newList5 = myList[:]
print(newList5)

print("----")
print(myList)
newList6 = myList[0:6:2]
print(newList6)

newList7 = myList[::2]
print(newList7)

newList8 = myList[1::2]
print(newList8)

print("----")
print(myList)
newList9 = myList[::-1]
print(newList9)

print("----")
weirdList = [1, 2, "Hi", True, 5.6, None]
print(weirdList)
weirdList[1] = False
print(weirdList)