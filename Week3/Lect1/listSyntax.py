L= [1,2, -10, 35, 100, -3]
print(L)

#weirdL= [1, "Hello", True, 12.0]
#print(weirdL)

print(len(L))
print(min(L))
print(max(L))
print(sum(L))

#Accessing Elements
print("Accessign Elements")
print(L[1])
print(L[-2])

print(L[::2])
print(L[::-1])

print("Retrieving elements")
for i in range(len(L)):
    print(L[i])
    
for e in L:
    print(e)
    
print("membership")
print(-3 in L)
print(-3 not in L)


#Modifying Elements
print(L)
L[2] = 34
print(L)

# Adding Elements
L.append(10)
print(L)

L.insert(2, -3)
print(L)

#removing elements
del L[3] # by Index
print(L)

del L[5:]
print(L)

L.remove(100) # by value
print(L)
print(len(L))

i= len(L)
L.insert(i, -3)
print(L)

L.remove(-3) # first occurance of the value
print(L)

e= L.pop() # last item
print(e)
print(L)

print("string <> lists")
s= "Hello, World"
ls= s.split(",")
print(ls)

lsc= list(s)
print(lsc)

print("".join(lsc))
print("-".join(lsc))

L1= [1,2,3]
L2= [4,5,6]
print(L1+L2)
print(L1)
print(L2)
print("----------")

print(id(L1))
L1= L1+L2
print(id(L1))
print(L1)
print(L2)

L1= [1,2,3]
L2= [4,5,6]

print("destructive extend")
print(id(L1))
L1.extend(L2)
print(id(L1))
print(L1)










