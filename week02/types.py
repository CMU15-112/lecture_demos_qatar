# Integer
a = 5
print(type(a))

# Floating Point
b = 5.0
print(type(b))

# Strings
c = "Cat"
print(type(c))
d = "5"
print(type(d))

# Booleans
e = True
print(type(e))
f = a > 5
print(f)
print(type(f))

##############

# Weirdly, functions are also types

def myFunction():
    print("Hi there!")
    
myFunction()
print(type(myFunction))

###############
# Two different ways to check if something is a specific type
print(type(a) == int)
print(isinstance(a, int)) # Use this one