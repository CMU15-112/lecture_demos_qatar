a= [[1,2],[3,4]]

# Access
print(a[0])
print(a[1][0])

# iterate over the elements
for r in a:
    print(r)
    for c in r:
        print(c)
        
#adding elements
a.append(5)
print(a)
a+=[6]
print(a)

a[1]+=[7]
a[0].append(8)
print(a)

# modifying elements
a[2]+=10
print(a)
a[0][1]= 20
print(a)
