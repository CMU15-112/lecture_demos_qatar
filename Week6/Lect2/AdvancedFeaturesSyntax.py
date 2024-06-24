import random

##### Default Variables/Arguments

# immutable data types
def f(x, y=10):
    return x+y

print(f(5))
print(f(5, 6))

# mutable data types
def f2(x, l=[]):
    l.append(x)
    return l

print(f2(2)) #creates the empty list l
print(f2(3)) #uses the one it created
print(f2(5))

# FIX for mutable data types
print("Fixing Mutable Optional Arguments")
def f3(x, l = None):
    if l == None:
        l = [] # creates a new empty list  
    l.append(x)
    return l

print(f3(2)) 
print(f3(3)) 
print(f3(5))

    
##### Variable number of arguments
print(2)
print("A", 1, [3], (4,5))

def longestWord(*args): 
    print(f"args: {args}, len: {len(args)}")
    longest = args[0]
    for w in args:
        if len(w) > len(longest):
            longest = w
            
    return longest
    
print(longestWord("Hello"))
print(longestWord("Hello", "World", "15112"))

L = ["Hello", "World", "15112"]
print(longestWord(*L))

##### Named Arguments

def vargsSample(x, y, r, **kwargs):
    print(f"kwargs: {kwargs}")
    
vargsSample(1, 2, 3, fill="black", border= True)


def vargsSample2(*args, **kwargs):
    print(f"args: {args}, len: {len(args)}")
    print(f"kwargs: {kwargs}")

vargsSample2(1,  fill="black", border= True)
vargsSample2(1, 2, 3, 4,  fill="black", border= True)

    
###### Functions As Arguments

def isBig(n):
    if n > 1000:
        return True
    return False

def filterList(l, f):
    ret = []
    for e in l:
        if f(e):
            ret.append(e)
    return ret

l= [457, 13, 3200, 1500]
print(filterList(l, isBig))


def getItem(t):
    return t[1]

L2 = [("C", 10), ("D", 5), ("A", 3)]
print(sorted(L2, key= getItem))

# Lambda Function: one-line function
print(sorted(L2, key= lambda t: t[1]))

# Sorting a list by Len 
L = [[5,4,3], [700], [4,7,1,3]]
L.sort(key= lambda L:len(L))
print(L)

# Sorting a list by median
def median(L):
    newList = sorted(L)
    mid = len(newList)//2
    
    if len(newList)%2 == 1:
        return newList[mid]
    else:
        return (newList[mid]+ newList[mid-1])//2
    
L.sort(key = median)
print(L)



#####  Function Decorators

def decorator(f): # takes a function as input and returns a function
    
    def decoratedF(*args): 
        print(f"before calling f")
        o= f(*args)
        print("after calling f")
        return o+1
        
    return decoratedF

# when we add this prefix,
    #python runs the decorated function instead of the original function 
@decorator
def f(x):
    print(f"called f {x}")
    return x*2
    
print(f(2))


###

# decorator function
def noneInsteadOfEmpty(f):
     def decoratedFunc(*args):
        L = f(*args)
        if len(L) == 0:
            return None
        else:
            return L
     return decoratedFunc   

@noneInsteadOfEmpty
def randomList():
    size  = random.randint(0,5)
    ret = []
    for i in range(size):
        ret.append(random.randint(0, 100))
    return ret

#for i in range(500):
 #   print(randomList())
  
@noneInsteadOfEmpty
def concatLists(L1, L2):
    return L1+L2

print(concatLists([1,2], [3,4]))
print(concatLists([],[]))


### logging decorator
def logging(f):
    def g(*args):
        print(f"Calling {f.__name__}{args}")
        o = f(*args)
        print(f"returned: {o}")
        return o
    
    return g


@logging
def myFunc(x, y):
    return x+y

myFunc(3,5)
        

    

