# basic Types
a = 2
print(type(a))

b = 2.0  #floats - decimals
print(type(b))

s = "CMU"
s1 = 'CMU'
print(type(s))
print(type(s1))
e = True
print(type(e))

print(5 > 3)
print(3 > 5)


### Function type
def f(x):
    return x*2

print(type(f))
print(type(f(2)))


### type checking
print(type(a) == int)
print(type(b) == int)

print(isinstance(a, int))
print(isinstance(b, bool))

