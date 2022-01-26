# Slicing
myList = ['a','b','c','d','e','f']
#indeces:  0   1   2   3   4   5

newList1 = myList[0:5]
print("newList1:",newList1)

newList1 = myList[0:1000]
print("newList1:",newList1)


newList2 = myList[2:7]
print("newList2:",newList2)
# c d e f

newList3 = myList[:7]
print("newList3:",newList3)
# all elements

newList4 = myList[0:7]
print("newList3:",newList4)
# all elements

newList5 = myList[3:]
print("newList3:",newList5)
# d e f

# Slicing won't give an error
newList5 = myList[10:13]
print("newList5:",newList5)



