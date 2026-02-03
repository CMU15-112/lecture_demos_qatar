### Merging Two Lists (Adding Elements From Another List)

print("Merging Lists ============= ")


### +
print("+ operation")
L1 = [1,2,3]
L2 = [4,5,6]
print(id(L1))
L1 = L1 + L2 # non-destructive
print(L1)
print(L2)
print(id(L1))


#### +=
print("+= operation")
L1 = [1,2,3]
L2 = [4,5,6]
print(id(L1))
L1+=L2 #destructive
print(id(L1))
print(L1)
print(L2)


#### extend
print("extend")
L1 = [1,2,3]
L2 = [4,5,6]
print(id(L1))
L1.extend(L2) #destructive
print(id(L1))
print(L1)
print(L2)

###### Sorting
print("Sorting ============= ")
L3 = [10, 100, 4, 50, 3, -1]
print(id(L3))
#seq - > list
L3 = sorted(L3, reverse = True)  #non-destructive
print(id(L3))

L3.sort() #destructive
print(L3)
print(id(L3))


###### Reversing
print("Reversing ============= ")
print(id(L3))
L3.reverse() #destructive
print(L3)
print(id(L3))

#slicing returns a new list
print(id(L3[::-1])) # non-destructive
print(id(L3[1:5])) 

##### Index/SLice Assignment
print("Index/SLice Assignment ============= ")
print(id(L3))
L3[1]= 3 #destructive
print(id(L3))

L3[2:4]= [5,6] #destructive
print(id(L3))

print(id(L3))

