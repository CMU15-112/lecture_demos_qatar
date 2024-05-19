s= "Hello, World"

for c in s:
    print(c)
    
print("Hello" in s)
print("world" in s)

print("H" not in s)


print("Numbers Fun")
sN="345"
print(sN.isdigit()) # all chars 0 - 9

fN= "34.5"
print(fN.isdigit())

n= int(sN)
print(n)
print(n+10)

f= float(fN)
print(f+3.4)

#opposite - number to str
nS= str(n)
print(nS)

print("Built-in Functions")

print(s.isalpha())
print("HelloWorld".isalpha())

print(s.isalnum())
print("HelloWorld123".isalnum())

print(s.isupper())
print("HELLOWORLD".isupper())
print("helloworld".islower())

s1= s.upper()
print(s1)
print(s)

print(s.lower())

print(s.replace("Hello", "Hi"))

sNew= "Hello, World, Hello"
print(sNew.replace("Hello", "Hi"))

print(s.count("o"))
print(s.find("World"))

print(s.split(","))
print(s.split())



