# Slicing
myList = ['a','b','c','d','e','f']
#indeces:  0   1   2   3   4   5

newList1 = myList[0:5]
print("newList1:",newList1)

newList2 = myList[2:7]
print("newList2:",newList2)

newList3 = myList[:5]
print("newList3:",newList3)

newList4 = myList[5:]
print("newList4:",newList4)

newList5 = myList[5:len(myList)]
print("newList5:",newList5)

newList6 = myList[5:5]
print("newList6:",newList6)

#elem = myList[len(myList)]
#elem = myList[20]

newList7 = myList[20:25]
print("newList7:",newList7)

newList8 = myList[2:7:2]
print("newList8:",newList8)

newList9 = myList[5:1:-1]
print("newList9:",newList9)
    
