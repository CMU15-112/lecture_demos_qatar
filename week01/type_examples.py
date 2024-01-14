# Integers
a = 5
print(type(a))

# Floating points
b = 5.0
print(type(b))

# Strings
c = "Cat"
print(type(c))

# Booleans
e = True
print(type(e))

def multiplyByNegativeOne(x):
    return -1*x

print(type(multiplyByNegativeOne))
print(type(multiplyByNegativeOne(4)))

# Imagine that I want to easily determine what type a holds
print(type(a) == int)
print(isinstance(a, int)) # Use this one
print(isinstance(b, float))