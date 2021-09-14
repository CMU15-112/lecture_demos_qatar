myList = [10, 20, 14, 8, 3, 2, 89, -100]
print(myList[0])
print(myList[4])
a = 3
print(myList[a])
print(myList[a+3])
#print(myList[8])
print(len(myList))
print(myList[-1])
print(myList[len(myList)-1])
#print(myList[-20])

print("---")
theSum = 0
for i in range(len(myList)):
    print(myList[i])
    theSum += myList[i]
print(theSum)

print("---")
for item in myList:
    print(item)
    
print("---")
myList.append(150)
print("Length of list", len(myList))
print(myList)
myList.insert(0, 200)
print(myList)
myList.insert(5, 210)
print(myList)
del myList[3]
print(myList)
del myList[3:5]
print(myList)
myList.remove(-100)
print(myList)

print("---")
newList = myList[0:3]
print(newList)

anotherList = myList[2:5]
print(anotherList)

evenList = myList[0:7:2]
print(evenList)

oddList = myList[1:7:2]
print(oddList)

print("---")
listA = myList[:4]
print(listA)

listB = myList[3:]
print(listB)

listC = myList[:]
print(listC)

print("---")
listD = myList[::-1]
print(listD)

print("---")
weirdList = [1,2,"Hi",True, 5.6, None]
print(weirdList)
