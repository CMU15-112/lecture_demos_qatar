#f(x) = 3 * x + 9
def f(x):
    return 3 * x + 9

print(f(2))
print(f(3))

def f1(x):
    print(3 * x + 9)
    return 3 * x + 9

print(f1(2))

def double(x):
    x*=2
    z = 9
    print("new x:", x)
    return x

print(double(2))

x = 1
y = double(x)
print("outside the function")
print(x)
#print(z)
