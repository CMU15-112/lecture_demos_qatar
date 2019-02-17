import copy

myList = [12, 14, 16, 30, 1, 3, 2]

for i in myList:
    print(i)
    
print("Item 0 is", myList[0])
print("Item 5 is", myList[5])
print("Last item is", myList[-1])

print("Slice:", myList[2:4])

print(myList)
myList = myList[0:2] + [30, 40] + myList[4:]
print(myList)

###

otherList = ["Hi", "word", "otherword"]
print(otherList)

###

yetAnotherList = [12, "hi", 4.56]
print(yetAnotherList)

###

def sumList(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]
    return sum
    
print(sumList([1,2.5,3.8,4,5,6]))

###
bList = [32,432,432,5344,2132,43,51]
print( sum(bList) )
print( min(bList) )
print( max(bList) )
print( sorted(bList) )

print(bList)
#bList.extend([67,56,78])
bList += [67,56,78]
print(bList)

print(bList)
bList = bList[0:5] + [1,2,3] + bList[5:]
print(bList)

###
myTuple = (1,2,3,4,5)
#myTuple[0] = 6

def myFunc(a):
    return 5,6
    
    
###

def weirdInt(i):
    i += 5


def weirdFunc(a):
    #a = a + [1,2,3]
    #a.extend([1,2,3])
    a += [1,2,3]
 
num = 10
print(num)
weirdInt(num)
print(num)

    
myList = [5,3,8]
print(myList)
weirdFunc(myList)
print(myList)


#myList = [5,3,8]
#b = myList
#b.append(6)
#print(myList)

a = [1,2,3]
b = copy.copy(a)

#Write the function alternatingSum(a) that takes a list of numbers and returns
#the alternating sum (where the sign alternates from positive to negative or
#vice versa). For example, alternatingSum([5,3,8,4]) returns 6 (that is,
#5-3+8-4).
def alternatingSum(a):
    pos = a[0::2]
    neg = a[1::2]
    
    res = sum(pos)
    res -= sum(neg)
        
    return res
    
def alternatingSum(a):
    res = 0
    for i in range(len(a)):
        if i%2 == 0:
            res += a[i]
        else:
            res -= a[i]
    
    return res
    
def alternatingSum(a):
    res = 0
    for i in range(0,len(a)):
        res += a[i]*( (-1)**i )
        
    return res
    
def alternatingSum(a):
    res = 0
    sign = 1
    for num in a:
        res += num*sign
        sign *= -1
        
    return res
    
#print( alternatingSum([5,3,8,4]) )

def isIncreasing(a):
    for i in range(1,len(a)):
        if a[i-1] > a[i]:
            return False
    return True
    
def isDecreasing(a):
    for i in range(1,len(a)):
        if a[i-1] < a[i]:
            return False
    return True
    
def isSorted(a):
    return isIncreasing(a) or isDecreasing(a)
    
print( isSorted([]) )
print( isSorted([1,2,3,4,5,6,7,8,9,10]) )
print( isSorted([1,2,3,4,5,6,7,8,9,10,9]) )
print( isSorted([2,1,2,3,4,5,6,7,8,9,10,9]) )
print( isSorted([10,8,6,4,3,1,-5]) )