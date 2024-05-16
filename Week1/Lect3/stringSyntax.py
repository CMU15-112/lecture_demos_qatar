s1 = "Hend"
print(s1)

s2= '112 Python'
print(s2)

print('Andrew says "Work Hard"')

# ASCII
print(ord('R'))
print(ord('z')-ord('a'))

# Length
print(len(s2))

# Indexing
print(s1[0])
print(s1[2])

print(s1[-1])
print(s1[-2])

# Slicing
print(s1[0:2])
print(s1[1:3])
print(s1[1:])
print(s1[:3])

print(s1[0:3:2])
print(s1[::2])

print(s1[::-1])

s= "Hello World"
print(s[1:8][::-1])
print(s[1:8][:2])

#Strings are immutable
#s[2]= 'a'

# replacing Char
newS= s[:2]+'a'+s[3:]
print(newS)

#iterating over characters
for i in range(len(s)): # hard
    print(s[i])
    
for c in s: # easy 
    print(c)
    
    





