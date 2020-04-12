# List comprehensions

L = [321, 312, 1, 2, 634789, 43, 92]
print(L)

#tripledList = []
#for item in L:
#    tripledList.append(3*item)

tripledList = [3*x for x in L]
print(tripledList)

evens = [x for x in L if x%2 == 0]
print(evens)
odds = [x for x in L if x%2 != 0]
print(odds)

tripledOdds = [3*x for x in L if x%2 != 0]
print(tripledOdds)

stringNumbers = [len(str(x)) for x in L]
print(stringNumbers)

L1 = [1,2,3]
L2 = [2,3,4,5]

bigList = [(x,y) for x in L1 for y in L2 if x != y]
print(bigList)

##################
print("---")
print(max(L))
print(max(3,8,10,4,7,20,30,5,67))
print("--")
def longestWord(*args):    
    if len(args) == 1 and isinstance(args[0], list):
        theList = args[0]
    else:
        theList = args
    
    result = -1
    for word in theList:
        if len(word) > result:
            result = len(word)
    if result == -1:
        return None
    else:
        return result

myList = ["test","monkey"]
print(longestWord("test","monkey"))
print(longestWord(myList))

#########
print("---")

def f(a,b,c):
    print("a",a)
    print("b",b)
    print("c",c)
    
def strangeArguments(a, b=10, **kwargs):
    print(a)
    print(b)
    print(kwargs)
    
strangeArguments(5,c=3,b=2,blah="Hi there")

######
print("---")
def f(a, b=10):
    return a+b

print(f(5))
print(f(5,6))

def listAppend(a, L=[]):
    L.append(a)
    return L

print(listAppend(6))
print(listAppend(15))

def listAppend(a, L=None):
    if L == None:
        L = []    
    L.append(a)
    return L

print(listAppend(6))
print(listAppend(15))

#################
print("---")

def doubler(x):
    return 2*x

def tripler(x):
    return 3*x

def sumWithOperation(myList, someFunc):
    result = 0
    for item in myList:
        result += someFunc(item)
    return result

print( sumWithOperation([1,2,4], tripler) )

print("---")

def sortingHelper(item):
    return len(item)

myStringList = ["happen", "gun", "smell", "organize", "complete", "quick",
                "rose", "qualify", "skin", "evanescent"]

myStringList.sort(key=sortingHelper)

for item in myStringList:
    print(item)
