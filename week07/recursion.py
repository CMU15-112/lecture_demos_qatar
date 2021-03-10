# x should be positive
def numSum(x):
    # Base Case
    if x <= 0:
        return 0
    # Recursive case
    return x + numSum(x-1)

print(numSum(5))
print(numSum(-1))

print("---")

def sumList(myList):
    print(myList)
    if len(myList) == 0:
        return 0
    elif len(myList) == 1:
        return myList[0]
    return myList[0] + sumList(myList[1:])

print(sumList([1,2,3,4]))

#bigList = list(range(0,3000))
#print(sumList(bigList))

print("---")

def sumListAgain(myList, depth=0):
    print(depth*"  ", myList)
    if len(myList) == 0:
        return 0
    elif len(myList) == 1:
        return myList[0]
    midpoint = len(myList)//2
    return sumListAgain(myList[:midpoint],depth+1) + sumListAgain(myList[midpoint:],depth+1)

print(sumListAgain([1,2,3,4,5,6,7,8,9,10,20,50,100]))

# bigList = list(range(0,100000000))
# print(sumListAgain(bigList))

# def sumDigits(n):
#     s = 0
#     while n > 0:
#         s += n%10
#         n //= 10
#     return s

print("---")

def sumDigits(n):
    if n == 0:
        return 0
    return n%10 + sumDigits(n//10)

print(sumDigits(12345))

print("---")

# Return the sum of the numbers in the range [a,b]
def rangeSum(a, b):
    if a > b:
        return rangeSum(b, a)
    elif a == b:
        return a
    
    return a + rangeSum(a+1,b)

print(rangeSum(5,6))
print(rangeSum(7,5))

print("---")

def rangeSumAgain(a, b):
    if a > b:
        return rangeSumAgain(b, a)
    elif a == b:
        return a
    splitPoint = (a+b)//2
    return rangeSumAgain(a,splitPoint) + rangeSumAgain(splitPoint+1,b)

print(rangeSumAgain(5,6))
print(rangeSumAgain(7,5))