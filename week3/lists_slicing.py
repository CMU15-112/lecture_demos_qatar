myList = ['a','b','c','d','e','f']
#indeces:  0   1   2   3   4   5

newList1 = myList[0:5]
print("newList1:",newList1)

newList2 = myList[2:7]
print("newList2:",newList2)

newList3 = myList[:7]
print("newList3:",newList3)

newList4 = myList[5:]
print("newList4:",newList4)

# Slicing won't give an error
newList5 = myList[10:13]
print("newList5:",newList5)