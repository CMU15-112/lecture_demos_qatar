myName = "Ryan Riley"
print(len(myName))
print(myName[0:5])
print(myName[::2])
print(myName[1::2])
print(myName[::-1])

print(myName[0])

# Strings are immutable, so you can't change them
#myName[0] = "T"
otherName = "T" + myName[1:]
print(otherName)
print(myName)

for i in range(len(myName)):
    print(myName[i])

print("---")

for c in myName:
    print(c)
    
print("---")

print(myName)
myName = "Bob" + myName[5:]
print(myName)

print(myName.isalpha())

myNum = "456"
print(myNum.isdigit())

myOtherNum = "4.56"
print(myOtherNum.isdigit())

print("---")
print(myName)
print(myName.lower())
print(myName)

print("---")
n = int("456")
numString = str(123.56)
print(numString + " Hi")
listString = str([5,6,7,8])
print(listString)

print("---")
print("Hi" + " " + "there")
#print("Hi" - "i")
#print("Hi" + 53)
print("Hi" + str(53))
print("Hello" * 5)