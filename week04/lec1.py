myName = "Ryan Riley"
print(len(myName))
print(myName[0:4])
print(myName[::2])
print(myName[::-1])

print(myName[3])

# Can't do this
#myName[3] = "t"

myName = myName[0:3] + "t" + myName[4:]
print(myName)

for i in range(len(myName)):
    print(myName[i])
    
for letter in myName:
    print(letter)
    
print(myName.lower())
print(myName)