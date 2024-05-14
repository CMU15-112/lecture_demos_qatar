# f(x) = 3 * x + 9

def f(x): 
    print("inside f")
    a = 3 * x + 9
    return a
    
print(f(2))
print(f(3))

y = f(2)+ 2
print(y)

def double(x):
    print("double")
    return 2*x

def otherDouble(x):
    print("other double")
    x*=2
    print(x)
    return x

b= double(100)
print(b)

c= 100
print(otherDouble(c))
print(c)

x= 100
print(otherDouble(x))
print(x)
