def foo(a, b):
    print(a)
    a = 4
    print("a =",a)
    return b
    print(b)

def bar(a):
    print("other", a%3)
    return a%3
    
a = 5
c = foo(a, 6)
print(a)
#print(b)
print("c=",c)
print(foo(1,bar(2)))