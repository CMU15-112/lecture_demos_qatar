### Defining 2D lists
a = [[1,2],
     [3,4]]

print(a)  #a = [[1,2], [3,4]] 

### Accessing Elements
print("Accessing Elements")
print(a[0])
print(a[1][0])

###  iterate over the elements
print("Iterating Over Elements")
for r in a: # iterates over rows (elements at the first dimension)
    for e in r:
        print(e)
    
        
### adding elements
print("Adding Elements")
a.append([5,6])
print(a)

a.append(5)
a+= [7]
print(a)

# at the second level
a[2].append(8)
a[1]+=[9]
print(a)


### modifying elements
print("Modifying Elements")
a[3]+=10
print(a)
a[0][1]=20
print(a)