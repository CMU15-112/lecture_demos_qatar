# we can use negative steps
l=list( range(99,0,-2) )
print(l)

# accessing elements by index (start counting from 0)
print("l[0] = ",l[0])

# we should be careful with the indeces (index out-of-bound error!)
#print("l[100] = ", l[100])
#print("l[50] = ", l[50])

print("l[49] = ", l[49])

# negative indeces
print("last elem = ", l[-1])

print("l[1] = ",l[ 1 ])

i = 10
print(type(i/2))

#indeces must be integers!
#print("l[i] = ",l[ i/2 ])

print("l[i] = ",l[ i//2 ])
