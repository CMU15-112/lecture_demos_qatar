print("L1+[4]---------------")
L1 = [1,2,3]
print(id(L1))
L1 = L1+[4]
print(id(L1))
print(L1)

print("L2+=[4] -----------")
L2= [4,5,6]
print(id(L2))
L2 +=[4]
print(id(L2))
print(L2)

# tuples are immutable lists
t= (7,8,9)
print(t)

# indexing and slicing
print(t[0])
print(t[1:])

t2= tuple(L2)
print(t2)

#t2[1]= 10 # immutable - crashes
#print(t2)

