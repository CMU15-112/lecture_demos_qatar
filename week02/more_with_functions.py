def multiplyByNegativeOne(x):
    a = 500
    x *= -1
    return x

a = 10
b = multiplyByNegativeOne(a)
print(a)
print(b)

###############

def myNewFunction(x, y, z):
    return 2*x + 3*y + z

c = myNewFunction(4,8,3)
print(c)

print("-----")

def myOtherNewFunction(x, y, z):
    a = myNewFunction(z,x,y)
    b = x + y + z
    return a,b

d,e = myOtherNewFunction(4,8,3)
print(d,e)