#https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

myNum = "456"
#print(myNum //2)

myInt = int(myNum)
print(type(myInt))
print(myInt//2)

myFloat = float(myNum)
print(myFloat)

myStr = str(myInt)
print(type(myStr))

alNum = "123Hello"
#print(int(alNum))
print(int(alNum[:3]))

## isdigit
print(alNum.isdigit())
print(myNum.isdigit())
print("24.5".isdigit())

### isalpha
print("Hello".isalpha())
print("Hello World".isalpha())

### isalnum
print(alNum.isalnum())

## isupper
print("HELLO".isupper())
print("hello".isupper())

##islower
print("hello".islower())



### creates a new string, which is a modified version of the original string

s = "Hi There"
## lower
print(s.lower())

## upper
print(s.upper())

print(s)
print()

## replace
print(s.replace("e", "a"))
print(s.replace("Hi", "Hello"))
print(s)
print()

s = s.replace("Hi", "Hello")
print(s)
print()


#### More Functions

s= "Hello, World!"

# count
print(s.count("o"))
print(s.count("World"))
print(s.count("O"))

print()

# find
print(s.find("o"))
print(s.find("World"))
print(s.find("O"))


# index
print(s.index("o"))
print(s.index("World"))
#print(s.index("O"))

# split
print(s.split(","))
for w in s.split(","):
    print(w)
    
print(s.split())

print(s.split("o"))

