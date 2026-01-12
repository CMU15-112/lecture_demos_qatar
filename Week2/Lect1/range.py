# range(n) --> [0, n-1]
for i in range(10): # [0, ..., 9]
    print(f"{i} squared = {i*i}")
    #print(i, "squared = ", i*i)
    
print("---------")
# range(s, n) --> [s, ..., n-1]
for i in range(2, 10): # [2, ..., 9]
    print(f"{i} squared = {i*i}")
    #print(i, "squared = ", i*i)
    

print("---------")
# raneg(s, n, step)
for i in range(2, 10, 2): # [2, 4, 6, 8]
    print(f"{i} squared = {i*i}")
    #print(i, "squared = ", i*i)

print("---------")
for i in range(10, 2):
    print(i)
    
print("---------")
for i in range(10, 2, -1):
    print(i)