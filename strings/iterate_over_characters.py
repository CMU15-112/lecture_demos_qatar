mystr="this is a text"

print("first letter: ", mystr[0])

print("last letter: ", mystr[-1])

print("first 4 letters: ", mystr[0:4])


for i in range(len(mystr)):
    print("letter ", i, mystr[i])
    
for c in mystr:
    if c == "i":
        print("I found i")
    print("letter ", c)


