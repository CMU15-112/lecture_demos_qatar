import copy

myList = [10, 20, 14, 8, 3, 2, 89, -100]
print(myList[0])
print(myList[3:5])

# Add to the existing list
myList.append(20)
print(myList)

# Create a new list
myList = myList + [45]
print(myList)

# Add to the existing list
myList += [56]

print("---")

def someFun(L):
    #L.append(45)
    L += [45]
    return L

a = [1, 2, 3, 4]
b = someFun(a)
print(a)
print(b)

print("---")

def someMoreFun(L):
    L = L + [45]
    return L

a = [1, 2, 3, 4]
b = someMoreFun(a)
print(a)
print(b)

print("---")
a = [1, 2, 3, 4]
b = a
b.append(5)
print(a)

print("---")
a = [1, 2, 3, 4]
b = copy.copy(a)
b.append(5)
print(a)

print("---")
a = [1, 2, 3, 4]
b = a[:]
b.append(5)
print(a)

print("---")

# Return the alternative sum of the list of numbers
# Example: [1, 2, 3, 4] == 1 - 2 + 3 - 4
def alternatingSum(theList):
    res = 0
    for i in range(len(theList)):
        if i % 2 == 0:
            res += theList[i]
        else:
            res -= theList[i]
    return res
print(alternatingSum([1,2,3,4]))

print("---")

def alternatingSumAgain(theList):
    res = 0
    flag = 1
    for num in theList:
        res += flag * num
        flag *= -1
    return res
print(alternatingSumAgain([1,2,3,4]))

print("---")
a = [4, 3, 2, 1]
# Destructive sorting
a.sort()

# Non-destructive sorting
a = [4, 3, 2, 1]
b = sorted(a)
print(a)
print(b)


print("---")


def ct1():
    alist = [4, 2, 8, 6, 5]
    blist = alist
    blist[3] = 999
    print(blist)
    print(alist)

print(ct1())


def f(L):
    L[0] = 15   
    L.append(1)   


def ct2(L):
    L += [1]
    M = L
    f(L)
    L = L + [1]
    if M is L:
        M[3] = 2
    print(L, M)


L = [0]
ct2(L)
print(L)







