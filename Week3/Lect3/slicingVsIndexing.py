s = "Hello"

#### normal
print(s[2])
print(s[1:4])

#### outside scope

# slicing doesn't crash (like range).. 
print(s[2:8])
print(s[8:10])

# indexing crashes
print(s[8]) 

