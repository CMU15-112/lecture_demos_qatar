def sum1toN(n):
    if n < 1:
        return None
    
    if n == 1:
        return 1
    else:
        return n + sum1toN(n-1)
    
print(sum1toN(1))
print(sum1toN(2))
print(sum1toN(20))
print(sum1toN(-5))


print("---")

def maxDigit(n):
    n = abs(n)
    if n < 10:
        return n
    else:
        curDigit = n % 10
        prevMax = maxDigit(n//10)
        return max(curDigit, prevMax)
    
print(maxDigit(1265427849347589431))
print(maxDigit(-123))

print("---")
def sumList(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + sumList(L[1:])
    
print(sumList([12,3,4,5]))
print(sumList([]))

print("---")
def maxValue(L):
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], maxValue(L[1:]))

print(maxValue([-1,-2,-5,-2,-6]))
print(maxValue([]))

print("---")
def maxValueAgain(L):
    if len(L) == 0:
        return None
    if len(L) == 1:
        return L[0]
    else:
        leftMax = maxValueAgain(L[:len(L)//2])
        rightMax = maxValueAgain(L[len(L)//2:])
        if leftMax > rightMax:
            return leftMax
        else:
            return rightMax
        
print(maxValueAgain([-1,-2,-5,-2,-6]))
print(maxValueAgain([-1,-2,-2,-6]))
print(maxValueAgain([]))
    
print("---")
# Return a list of all the odd values in L
def oddValues(L):
    if len(L) == 0:
        return []
    elif len(L) == 1 and L[0] % 2 == 1:
        return [L[0]]
    elif len(L) == 1 and L[0] % 2 == 0:
        return []
    elif len(L) > 1 and L[0] % 2 == 1:
        return [L[0]] + oddValues(L[1:])
    else:
        return oddValues(L[1:])
    
print(oddValues([423,4,32,427,5346,45]))
print(oddValues([4,32,5346]))
print(oddValues([]))
print(oddValues([-5, -6]))
print(oddValues([423]))
print(oddValues([42]))

print("---")

# Assuming L1 and L2 are lists of integers,
# return an interleaved list.
# Example:
# L1 = [1,2,3]
# L2 = [4,5,6]
# Return is [1,4,2,5,3,6]
def interleave(L1, L2):
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    else:
        return [L1[0]] + [L2[0]] + interleave(L1[1:], L2[1:])
    
print(interleave([1,2,3],[4,5,6]))
print(interleave([1,2,3],[6,7,8,9,10]))

print("---")

def reverseString(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverseString(s[:-1])
    
print(reverseString("hithere"))
print(reverseString(""))
