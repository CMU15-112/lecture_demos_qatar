def makeNegative(x):
    a = 100
    b = 200
    x *= -1
    return x

a = 10
b = makeNegative(a)
print(b)
print(a)

x = 20
y = makeNegative(x)
print(x)
print(y)
print(a)
print(b)

def myNewFunction(x, y, z):
    return 2 * x + 3 * y + z

print(myNewFunction(1,2,3))

def myOtherFunction(x, y, z):
    a = myNewFunction(x,y,z)
    b = x + y + x
    return a,b

d, e = myOtherFunction(1,2,3) 
print(d)
print(e)