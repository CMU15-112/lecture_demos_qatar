myName = "Ryan Riley"
myNameLength = len(myName)
print(myName, myNameLength)

# Indexing and slicing
print(myName[3])
print(myName[0:6])
print(myName[0:7])
print(myName[3:])
print(myName[:8])
print(myName[0:9:3])
print(myName[::2])
print(myName[-1])
print(myName[::-1])

# Strings are immutable
myString = "Hi there"
#myString[1] = 'c'
myNewString = myString[0] + 'c' + myString[2:]
print(myNewString)

# Looping through strings
for i in range(len(myName)):
    print(myName[i])
    
print("---")

for c in myName:
    print(c)
    
print("---")

# Some helper functions
if myName.isalpha():
    print("The name is entirely alphabetic")
else:
    print("The name is not entirely alphabetic")
    
print(myName.lower())
print(myName.upper())

# Number play
myNum = "456"
print(myNum.isdigit())
myFloatingNum = "4.56"
print(myFloatingNum.isdigit())

x = int(myNum)
print(x + 1)
y = float(myFloatingNum)
print(y)

s = str(453)
print(s)

# Checking string contents
s1 = "my"
s2 = "hi there my name is joe"
if s1 in s2:
    print("I found the substring")

