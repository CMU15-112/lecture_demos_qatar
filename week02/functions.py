def multiplyByNegativeOne(x):
    x *= -1
    return x

def otherMultiply(x):
    x *= -1
    print(x)
    
a = 10
b = multiplyByNegativeOne(a)
print(a)
print(b)

print("==========")

c = 10
d = otherMultiply(a)
print(c)
print(d)
