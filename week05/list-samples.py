myList = [10, 20, 14, 8, 3, 2, 89, -100]
print(myList[0])
print(myList[4])
a = 3
print(myList[a])
print(myList[a+3])
print(len(myList))
print(myList[-1])

theSum = 0
for i in range(len(myList)):
    theSum += myList[i]
print(theSum)

theSum = 0
for item in myList:
    theSum += item
print(theSum)

# Useful methods
myList.append(150)
print(myList)
myList += [160]
print(myList)
myList.insert(3, 78)
print(myList)
myList.insert(0, -1)
print(myList)
myList.insert(-1, 175) # Maybe not so weird
print(myList)
del myList[2]
print(myList)
del myList[3:5]
print(myList)
myList.append(89)
myList.append(89)
print(myList)
myList.remove(89)
print(myList)
item = myList.pop()
print(item)
item = myList.pop(5)
print(item)
print(myList)

###

newList = myList[0:3]
print(newList)

newList = myList[0:7:2]
print(newList)

newList = myList[::-1]
print(newList)

###

weirdList = [1, 2, "Hi", True, 5.6, None]
print(weirdList)

# Exercise: Alternating Sum
# Given a list of integers, calculate the alternating sum
# [1, 2, 3, 4] = 1 - 2 + 3 - 4 = -2
# Observation: 1 + -2 + 3 + -4

def alternatingSum(theList):
    theSum = 0
    for i in range(len(theList)):
        if i % 2 == 1:
            theSum -= theList[i]
        else:
            theSum += theList[i]
    return theSum

def alternatingSum(theList):
    theSum = 0
    sign = 1
    for number in theList:
        theSum += number*sign
        sign = -sign
    return theSum

def alternatingSum(theList):
    return sum(theList[0::2]) - sum(theList[1::2])

print("Testing alternatingSum...", end="")
assert alternatingSum([1,2,3,4]) == -2
print("pass")

# Destructive vs Non-destructive
a = [15]
b = [35]

# Destructive
a.append(1)
a += [2]

# Non-destructive
c = a + [3]
a = a + [7]

# Destructive
a.extend([4,5])
a += [6,7]
print(a)

# Whoops
a + [10]

# Most builtin methods that somelist.something() are destructive
a.remove(5)

# Non-destructive, makes a sorted copy
d = sorted(a)

# Destructive
a.sort()