def f(x):
    print("A:",x)
    b = x + 5
    print("B:",x)
    x = b
    return x + 6

def g(x):
    print("C:",x)
    b = f(x)
    print("D:",x)
    x = b
    return x + 3

x = 10
print("E:",x)
a = g(x)
print("F:",x)
print("final a=",a)
print("final x=",x)
