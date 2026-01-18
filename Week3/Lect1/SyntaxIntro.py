s1  = "Python"
print(s1)

s2 = "112 Python"
print(type(s2))

print("Andrew Says: 'Work Hard' ")


##ord
print(ord('R'))
print(ord('r'))
print(ord('Z')-ord('A'))
print(ord('Z')>ord('A'))

##len
print(len(s1))

### Slicing and Indexing
print(s2[0])
print(s2[5])

print(s2[-1])
print(s2[-3])

## Slicing
print(s2[0:5])
print(s2[2:8])
print(s2[:7])
print(s2[2:])

print(s2[0:8:3])
print(s2[::3])

print(s2[::-1])


# Double Slicing
print(s2[1:8][::-1])
print(s2[1:8][5])
print(s2[1:8][:2])

myS = "Hi There"
#myS[1] = "c"
myS = myS[0] + "c" + myS[2:]
print(myS)


#### String Operations
s = "CS"+ " " + "112"
print(s)

## repition
s = "ha"*3
print(s)

### Checking Memcership
s = "Hello World"
print("l" in s)
print("W" not in s)
print("World" in s)

## Iterating over chars

#hard
for i in range(len(s)):
    print(s[i])

print()
# easy
for c in s:
    print(c)
    
