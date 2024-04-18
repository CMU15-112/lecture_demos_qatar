def f(x, y=10):
    return x + y

print(f(5))
print(f(5,6))

def f(x, L=[]):
    L.append(x)
    return L

print(f(1))
print(f(2))
print(f(33))

def f(x, L=None):
    if L == None:
        L = []
    L.append(x)
    return L

######

print("bob")
print("bob", 5, True, 10)

# Return the longest word passed as an argument
def longestWord(*args):
    res = args[0]
    for word in args:
        if len(word) > len(res):
            res = word
    return res
    
print(longestWord("this", "is", "really", "nice"))

myWords = ["this", "is", "really", "nice"]
print(longestWord(*myWords))

###

def vargsSample(x, y, r, **kwargs):
    print(f"{x} {y} {r} {kwargs}")
    
vargsSample(5, 10, 2.5, fill='black', dashes=False)

def vargsSample(*args, **kwargs):
    print(f"{args} {kwargs}")
    
vargsSample(5, 10, 2.5, fill='black', dashes=False)

###

def filterList(L, f):
    ret = []
    for item in L:
        if f(item):
            ret.append(item)
    return ret

def isBig(x):
    if x > 1000:
        return True
    else:
        return False

L = [457, 4326, 786, 1657]
newList = filterList(L, isBig)
print(newList)

def getItem(t):
    return t[1]

L = [("Dogs", 5), ("Cats", 2), ("Falcons", 3)]
newList = sorted(L, key=getItem)
print(newList)

newList = sorted(L, key=lambda t: t[1])
print(newList)

L = [[5, 4, 3], [700], [4, 7, 1, 3]]
L.sort(key=lambda L: len(L))
print(L)

def median(L):
    # Return the median L
    newList = sorted(L)
    mid = len(newList)//2
    if len(newList)%2 == 1:
        return newList[mid]
    else:
        return (newList[mid] + newList[mid-1])/2
    pass

print(median([21,312,1,4,5]))
print(median([21,312,1,4]))

L.sort(key=median)
print(L)

###

def noneInsteadOfEmpty(f):
    def g(*args):
        L = f(*args)
        if len(L) == 0:
            return None
        else:
            return L
    return g

import random

@noneInsteadOfEmpty
def generateRandomList():
    size = random.randint(0, 5)
    ret = []
    for i in range(size):
        ret.append(random.randint(0, 100))
    return ret

#for i in range(500):
#    print(generateRandomList())
    
@noneInsteadOfEmpty
def concatLists(L1, L2):
    return L1+L2

print(concatLists([1,2],[3,4]))
print(concatLists([],[]))


###

def logging(f):
    def g(*args):
        print(f"Calling {f.__name__}{args}")
        ret = f(*args)
        print(f"returned: {ret}")
        return ret
    return g

@logging
def myFunc(x, y):
    return x+y

v = 0
for i in range(2):
    for j in range(2):
        v += myFunc(i, j)
print(v)