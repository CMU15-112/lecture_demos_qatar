myList = ['a','b','c','d','e','f']
myList.remove('a')
print(myList)

#myList.remove('a')  # ups, crash
#print(myList)

item = myList.pop(3)
print("Extracted item at index 3 (", item ,") from" ,myList)

item = myList.pop()
print("Extracted item at last index (", item ,") from" ,myList)
