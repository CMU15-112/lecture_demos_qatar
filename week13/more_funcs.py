import copy

# Named, default arguments
def f(x, y = 10, z = 8):
    return x + y + z

print(f(6))
print(f(6, 1, 2))
print(f(6, 1))
print(f(6, z = 2, y = 1))
print(f(z = 2, y = 1, x = 6))

def f(x, L = []):
    L.append(x)
    return L

print(f(1))
print(f(2))

def f(x, L = None):
    if L == None:
        L = []
    L.append(x)
    return L

print(f(1))
print(f(2))

# Variadic function
print("Bob")
print("Bob", 5, 10, 4.1, True)

def longestWord(*args):
    if len(args) == 0:
        return None
    result = args[0]
    for word in args:
        if len(word) > len(result):
            result = word
    return result

print(longestWord("this", "is", "really", "nice"))
print(longestWord())

myWords = ["this", "is", "really", "nice"]
print(longestWord(*myWords))

def weird(x, y, *args):
    print(x, y)
    print(args)
    
weird(1, 2)

def vargSample(x, y, **kwargs):
    print(x, y)
    print(kwargs)
    
vargSample(4, 5, bob = 56, cat = "dog")

# Whoa.
def weird(*other, **other2):
    print(other)
    print(other2)

weird(4, 5, bob = 56, cat = "dog")

def filterList(L, f):
    ret = []
    for item in L:
        if f(item):
            ret.append(item)
    return ret

def isBig(x):
    if x > 1000:
        return True
    return False

L = [457, 4326, 786, 1657]
newList = filterList(L, isBig)
print(newList)

def getItem(t):
    return t[1]

L = [("Dogs", 2), ("Cats", 1), ("Falcons", 3)]

print(sorted(L, key=getItem))

# Lambda function
L = [1,2,3,4,5,6,7,8]
newList = filterList(L, lambda x: True if x % 2 == 0 else False)
print(newList)

L = [("Dogs", 2), ("Cats", 1), ("Falcons", 3)]
print(sorted(L, key= lambda t: t[1]))

myFunc = lambda x, y, z: x+y+z
print(myFunc(1,2,3))

L = [[5,4,3], [700], [4,7,1,3]]
# Sort it by...
# 1. The number of items in the list (use lambda function)
print(sorted(L, key = lambda x: len(x)))
# 2. The median value of each list (maybe use a regular function)
def median(x):
    if len(x) % 2 == 1:
        return sorted(x)[len(x)//2]
    else:
        return (sorted(x)[len(x)//2]+sorted(x)[len(x)//2 - 1])/2
    
print(sorted(L, key=median))
# Sort by the media of each list
print(sorted(L, key = lambda x: sorted(x)[len(x)//2] if len(x) % 2 == 1 else (sorted(x)[len(x)//2]+sorted(x)[len(x)//2 - 1])/2))
print(sorted(L, key = lambda x: (sorted(x)[len(x)//2] + sorted(x)[(len(x)-1)//2])/2))

def noneInsteadOfEmpty(f):
    def g(*args):
        L = f(*args)
        if type(L) == list and len(L) == 0:
            return None
        else:
            return L
    return g

import random
@noneInsteadOfEmpty
def generateRandomList():
    ret = []
    size = random.randint(0, 5)
    for i in range(size):
        ret.append(random.randint(0, 100))
    return ret

for _ in range(500):
    print(generateRandomList())