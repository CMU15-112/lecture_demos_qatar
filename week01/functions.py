# Functions are a mathematic concent
# f(x) = 5 * x + 8
# y = f(8) + 9

def multiplyByNegativeOne(x):
    return -1*x

def otherMultiplyByNegativeOne(x):
    x *= -1
    return x

a = 10
b = multiplyByNegativeOne(a)
print(a)
print(b)

# A copy of c is passed into the function, not c itself
c = 10
d = otherMultiplyByNegativeOne(c)
print(c)
print(d)