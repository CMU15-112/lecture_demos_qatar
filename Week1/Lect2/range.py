for i in range(10):
    print(i, " squared = ", (i*i))
    
print("starting at 2")
for i in range(2, 10):
    print(i, " squared = ", (i*i))

print("another attempt")
for i in range(10, 2):
    print(i, " squared = ", (i*i))
    
    
print("step = 2")
for i in range(2, 10, 2): #step=2
    print(i, " squared = ", (i*i))
    

print("step = -2")
for i in range(10, 2, -2): #step=2
    print(i, " squared = ", (i*i))
    
print("step = -2")
for i in range(2, 8, 2): #step=2
    print(i, " squared = ", (i*i))