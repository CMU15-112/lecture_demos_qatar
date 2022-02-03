myList = ['a', 'b', 'c', 'a', 'd', 'e', 'f', 'x', 'y', 'z']
myList.remove('a')
myList.remove('y')
#myList.remove('y')
print(myList)

item = myList.pop()
print(myList)

item = myList.pop(0)
item = myList.pop(6)
print(myList)

