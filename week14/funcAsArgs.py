def square(x):
    return x * x

def derivative(f, x):
    h = 10**-10
    return (f(x+h) - f(x))/h


print(derivative(square, 42))
# with lambda we can create a function on the spot
print(derivative(lambda x: x**3, 5))

cube = lambda x: x**3

print(cube(3))
