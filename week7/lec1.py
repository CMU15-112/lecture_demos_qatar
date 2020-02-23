def f1(x):
    # Base Case
    if (x == 0):
        return 0
    # Recursive Case
    else:
        return 1 + f1(x-1)
    
#print(f1(3))

def f2(x):
    if (x == 10):
        return
    
    print(x)
    f2(x+1)
    
#f2(1)

#print("---")

def sumList(myList):
    # Base Case
    if len(myList) == 0:
        return 0
    # Recursive Case
    return myList[0] + sumList(myList[1:])

print(sumList([1,2,3]))

# Sum all of the digits of integer n
def sumDigits(n):
    # Base Case
    if n < 10:
        return n
    # Recursive Case
    return n%10 + sumDigits(n//10)

print(sumDigits(12345))

# Return the sum of all the digits in the range [a,b]
def rangeSum(a, b):
    # A little hack to handle cases like [5,2]
    if a > b:
        return rangeSum(b,a)
    
    # Base Case
    if a == b:
        return b
    # Recursive Case
    return a + rangeSum(a+1,b)

print("---")
print(rangeSum(2,5))
print(rangeSum(5,2))

def sumListAgain(myList):
    # Base Case
    if len(myList) == 1:
        return myList[0]
    # Recursive Case
    midPoint = len(myList)//2
    return sumListAgain(myList[:midPoint]) + sumListAgain(myList[midPoint:])

print("---")
myList = list(range(5,3000))
print(sumListAgain(myList))
#print(sumList(myList))

# Return the sum of all the digits in the range [a,b]
def rangeSumAgain(a, b):
    # A little hack to handle cases like [5,2]
    if a > b:
        return rangeSumAgain(b,a)
    
    # Base Case
    if a == b:
        return b
    # Recursive Case
    splitPoint = (a+b)//2
    return rangeSumAgain(a,splitPoint) + rangeSumAgain(splitPoint+1,b)

print("---")
print(rangeSumAgain(2,5))
print(rangeSumAgain(5,2))