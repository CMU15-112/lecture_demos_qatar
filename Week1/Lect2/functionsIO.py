def f(x, y, z):
    return x + y + z

def g():
    return 42, 5

def h():
    print("Hello World!")

###main program
print(f(1,2,3))
a, b = g()
print(a)
print(b)
print(h())

## number of args = number of params
#f(1,2)
#g(1)