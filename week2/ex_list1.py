

myList = ['a','b','c','d','e','f']
#indeces:  0   1   2   3   4   5


print(myList[4])

print(myList[1])
print(myList[0])
print(type(myList))
print(type(myList[0]))

print(myList[-1])
print(myList[-2])


myList = ['a','b','c','d','e','f']
for i in range(len(myList)):
    print("++ ", myList[i])
    
    
for item in myList:
    print(item)
