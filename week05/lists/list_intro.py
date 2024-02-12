myList = [10, 20, 14, 8, 3, 2, 56, -3]
print(myList)
print(myList[0])
a = 3
print(myList[a])
print(myList[a+3])

print(len(myList))

print(myList[-1])

print("########")

for i in range(len(myList)):
    print(myList[i])
    
for e in myList:
    print(e)
    
print("########")

myList.append(150)
print(myList)
myList.insert(5, 200)
print(myList)
del myList[2]
print(myList)
del myList[2:5]
print(myList)
#del myList[::2]
#print(myList)
myList.append(56)
print(myList)
myList.remove(56)
print(myList)
a = myList.pop()
print(a)
print(myList)

# Slicing works just like strings

# You can do this, but you probably shouldn't...
weirdList = [1, 2, "Hi", True, 5.6, None]
print(weirdList)
