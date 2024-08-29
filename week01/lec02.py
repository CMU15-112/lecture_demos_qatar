# Operations
a = 7
b = 12

print(a+b)
print(b-a)
print(b / a)
print(a ** b)

print("---")

print(b // a)
print(b % a)

c = 5
d = 6
e = 3
print(c & d)
print(c | d)
print(c ^ d)
print(e << 1)
print(e >> 1)

# Precendence
a = 6 + 3 * 4 - 6 / 3
print(a)

c = 5 - 4 - 3
print(c)

d = 2 ** (3 ** 4)
print(d)

e =  (2 ** (3 ** 4)) - 3 / 2
print(e)

# Variables

# Name your variables like this
ageOfTeacher = 42

# Don't do this in 15-112
age_of_teacher = 42

# Don't do this anywhere
ageofteacher = 42

ageOfTeacher1 = 40
ageOfTeacher2 = 45

# You can redefine variables, but this is dangerous
a = 10
a = "Ryan"

x = 10
x = x + 1
x += 1
x *= 5
x //= 3

# Python doesn't save you from stupid
print(x)
x = x + 5
print(x)

# Functions
def multiplyByNegativeOne(x):
    x *= -1
    return x

def testFunc(x):
    x *= -1
    print(x)

a = 10
b = multiplyByNegativeOne(a)
print(a)
print(b)

b = testFunc(a)
print(b)

# Types
a = 5
print(type(a))

b = 5.0
print(type(b))

c = "Ryan"
print(type(c))

d = True
print(type(d))

e = a < 1
print(e)
print(type(e))

f = "5"
print(type(f))
#print(f + 10)

print(type(None))

print(type(int))

print(type(multiplyByNegativeOne))

print(type(print))

# WTH? You don't need to know this
print(type(type(int)))
print(type(type))

myVar = 10

print(type(myVar) == int)
print(type(myVar) == float)
print(type(myVar) == str)

print(isinstance(myVar, int))
