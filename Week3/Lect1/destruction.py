L1= [1,2,3]
L2= [4,5,6]

print("non-destructive L1+L2")
print(id(L1)) # memory address of L1
L1= L1+L2 
print(id(L1)) # address changes 
print(L1)
print(L2)

L1= [1,2,3]
L2= [4,5,6]

print("destructive extend")
print(id(L1))
L1.extend(L2) 
print(id(L1))  # address does not change
print(L1)

print("append")
print(L2)
L2.append(15) # destructive
print(L2)

print("L2+[16]")
L2+[16] # non-destructive 
print(L2)

print("L2= L2+[16]")
L2= L2+[16] # non-destructive
print(L2)

L3= [10, 100, 4, 50, 3, -1]
print("sorted() ")
c= sorted(L3) # non-detructive
print(f"L3: {L3}")
print(c)

print("sort()")
print(L3)
L3.sort() # destructive
print(L3)

print("reverse()")
L3.reverse() # destructive
print(L3)

#modifying elements using index or slice range is destructive
L3[1]= 10
print(L3)

L3[2:4]= [11, 5]
print(L3)


