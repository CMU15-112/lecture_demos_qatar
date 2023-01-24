myList = ['a','b','c','d','e','f']
#indeces:  0   1   2   3   4   5

myList[2] = 'cmu'
print(myList)

del myList[2]
print(myList)

myList.pop()  # removes the last
print(myList)

myList.pop(1)  # removes the element at index 1 (b)
print(myList)
