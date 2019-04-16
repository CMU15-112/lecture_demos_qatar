def func1(*a):
    print(a)
    
func1(1,2,3,4,5)
    
def func2(a, b, c):
    print(a,b,c)
    
myList = [1,2,3]
func2(*myList)

def func3(x, **a):
    print(x)
    print(a)
    
func3(8, a=1,b=2,myotherarg=3)
#This doesn't work:
#func3(8,1,2)

def func4(x=0, a=6, b=7):
    print(x,a,b)
    
func4()
func4(5, b=20)
func4(x=5, b=20)
d = {"x":5, "a":10, "b":15}
func4(**d)
myList = [5,10,15]
func4(*myList)

def doubler(f, x):
    return f(x)*2
    
def func5(x):
    return x+10

print(doubler(func5, 5))

def derivative(f, x):
    h = 10 ** -8
    return (f(x+h)-f(x))/h
    
def f1(x):
    return 4*x**2 + 3*x + 3
    
print(derivative(f1, 10))

def derivativeFn(f):
    def g(x):
        h = 10 ** -5
        return (f(x+h)-f(x))/h
    return g

fprime = derivativeFn(f1)
fprimeprime = derivativeFn(fprime)
print(fprime(10))
print(fprimeprime(10))

f2 = lambda x: 6*x**3 + 5*x**2 + 6*x + 9
print(f2(5))
f2p = derivativeFn(f2)
print(f2p(5))
f2pp = derivativeFn(f2p)
print(f2pp(5))

g = derivativeFn(lambda x: 6*x**3 + 5*x**2 + 6*x + 9)
print(g(5))

f3 = lambda x,y: x**2+y**2
"""
def f3(x,y)
    return x**2+y**2
"""
print(f3(3,4))

def newDoubler(f):
    def g(x):
        return f(x)*2
    return g
    
f4 = lambda x: x+25
f5 = newDoubler(f4)
print(f5(5))

@newDoubler
def f6(x):
    return x+10
    
print(f6(5))

def f7(x):
    return x+10
f7 = newDoubler(f7)

print(f7(5))

def f8(x, lst=[]):
    lst.append(x)
    return lst
    
myList = f8(5)
myList = f8(10, myList)
print(myList)

myOtherList = f8(15)
print(myOtherList)

def f9(x, lst=None):
    if lst == None:
        lst = []
        
    lst.append(x)
    return lst
    
myList = f9(5)
myList = f9(10, myList)
print(myList)

myOtherList = f9(15)
print(myOtherList)