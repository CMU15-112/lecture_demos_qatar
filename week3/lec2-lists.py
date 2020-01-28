myList = [10, 20, 14, 8, 3, 2, 89, -100]
print(myList)
print(myList[4])
print(myList[4] + myList[6])
print(len(myList))

print("---")
for i in range(len(myList)):
    print(myList[i])
    
print("---")
for bob in myList:
    print(bob)
    
for i in range(len(myList)):
    myList[i] += 1

print("---")
print(myList)

print(myList[-1])
print(myList[len(myList)-1])

print(myList[-2])

#print(myList[8])

###

print(myList[2:6])
print(myList[:6])
print(myList[3:])
print(myList[:])
print(myList[::3])

####
anotherList = [1, 2, 3, 4, 3, 2, 1]
print(sum(anotherList))
print(max(anotherList))
print(min(anotherList))
print(sorted(anotherList))

###
print("---")

theList = [1, 2, "Hi", True, 5.6]
theNextList = theList

print(theList)
print(theNextList)
theNextList[0] = "Bob"
print(theList)
print(theNextList)

print("---")

theList = [1, 2, "Hi", True, 5.6]
theNextList = theList[:]

print(theList)
print(theNextList)
theNextList[0] = "Bob"
print(theList)
print(theNextList)