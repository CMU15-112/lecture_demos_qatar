import math

a = 0.1
print(a == 0.1)

b = 0.1 + 0.1
print(b == 0.2)

c = 0.1 + 0.1 + 0.1
print(c == 0.3)

a += 0.1
print(a == 0.2)

a += 0.1
print(a == 0.3)

print(a)
print(b)
print(c)

print(math.isclose(a, 0.3))

# This is, roughly, what math.isclose does
def myIsClose(x,otherValue):
    return abs(x-otherValue) < 0.000001

print(myIsClose(a,0.3))