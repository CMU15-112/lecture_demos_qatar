import math

a = 7
b = 12

print(a // b)


c = 6 + 3 * 4 - 6 / 3
print(c)

e = 2 ** (3 ** 4)
print(e)

ageOfTeacher = 44

x = 10
x = x + 1
x += 1
x -= 5
x **= 2
print(x)

print("---")

def multiplyByNegativeOne(x):
    print("hi there")
    x *= -1
    return x

x = 10
y = multiplyByNegativeOne(x)
print(y)
print(x)


print("---")

a = 5
print(type(a))

b = 5.0
print(type(b))

c = "Hi there bob"
print(type(c))

d = True
print(type(d))
e = a < 10
print(e)

def myFunction():
    print("Hi there!")
    
print(type(myFunction))

f = "True"
f = "56"

print("---")
print(type(a) == int)
print(type(a) == float)

print(isinstance(a, int))

print("---")

a = 0.1 + 0.1 + 0.1
print(a)
print(a == 0.3)
print(a - 0.3 < 0.00000001)
print(math.isclose(a, 0.3))
