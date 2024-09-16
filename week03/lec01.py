myName = "Ryan_Riley"
myName = myName + " is a professor"
print(myName)

b = myName[0:4]
print(b)

c = myName[0:6:2]
print(c)

print(myName[8:0:-1])

print(myName[::])

print(myName[::2])

print(myName[1::2])

print(myName[::-1])

print(myName[4])

print(myName[-3])

# This is not allowed
#myName[3] = "g"

# What if I wanted to?
myName = myName[0:3] + "g" + myName[4::]
print(myName)

print(len(myName))

for i in range(len(myName)):
    print(myName[i])
    
for c in myName:
    print(c)
    
print("---")

myNum = "456.4"
print(myNum.isdigit())

other = "fsdFds"
print(other.isalpha())

print(other.lower())

myNum = "1234"
n = int(myNum)
print(n+1)

s = str(42)
print(s + "hi")

print(myName.replace("e","6"))
