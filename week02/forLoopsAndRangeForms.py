#range(max) : [0, max)
print(" form 1:")
for i in range(11):
    print(i)
    
#range(min, max): [min, max)
print(" form 2:")
for i in range(1, 11):
    print(i, "squared = ", (i*i))

#range(min, max, step): [min, min+step, ..., max)
print("form 3")
for i in range(2, 11, 2):
    print(i, "squared = ", (i*i))
    
# range(max, min, -step): [max, max-step, ..., min)
print("form 4")
for i in range(10, 0, -2):
    print(i, "squared = ", (i*i))
    
