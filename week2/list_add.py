# With extend
myList = ['a','b','c','d','e','f']
myList.extend(['x','y', 'z'])

myList.extend(['o'])
myList.append('o')

print(myList)

# With += operator
myList += ['cmu', '15112']
print(myList)

# You can use += to add a single element
myList += ['hello']
print(myList)