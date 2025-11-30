def square(x):
    return x * x


print(square)        # <function square at ...>
print(type(square))  # <class 'function'>

# we can assign functions to variables
cube = square
square = "Hello"

print(type(square))
print(cube(3))

print(sum([1,2]))



print(sum([1,2])) # this would fail

def mySum(L):
    return 42

__builtins__.sum = mySum

print(sum([1,2]))
