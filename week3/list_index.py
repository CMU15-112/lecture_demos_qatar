myList = ['a', 'b', 'c', 'a', 'd', 'a', 'a', 'e']
#indeces:  0    1    2    3    4    5    6    7

print("myList      =", myList)
print("2 in myList =", (2 in myList))
print("4 in myList =", (4 in myList))

print("2 not in myList =", (2 not in myList))
print("4 not in myList =", (4 not in myList))


print("myList.count('a') =", myList.count('a'))
print("myList.count('b') =", myList.count('b'))
print("myList.count('c') =", myList.count('c'))


print("myList.index('d')   =", myList.index('d'))
print("myList.index('a')   =", myList.index('a'))
print("myList.index('a',1) =", myList.index('a',1))
print("myList.index('a',4) =", myList.index('a',4))

if 'z' in myList:
    print("myList.index('z')   =", myList.index('z'))