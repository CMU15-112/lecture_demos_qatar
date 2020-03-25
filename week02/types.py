# Integer
a = 5
print(type(a))

# Floating Point
b = 5.3
print(type(b))

# Strings
c = "Cat"
d = 'Cat'
e = """Cat"""
f = '''Cat'''
print(type(c))

# Booleans
g = a > 6
print(g)
h = True
i = False
print(type(g))

# Functions are also type
def myFunction():
    print("Hello!")
    
print(type(myFunction))

# Usage of type
print(type(a) == bool)
