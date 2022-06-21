"""Without using strings, write the recursive function
onlyOddDigits(L), that takes a list L of non-negative
integers (you may assume that), and returns a
new list of the same numbers only without their even
digits (if that leaves no digits, then replace the number with 0).
So: onlyOddDigits([43, 23265, 28,
58344]) returns [3, 35, 0, 53].
Also the function returns the empty list if the original list is empty.
Remember to not use strings.
"""

def removeOddDigits(n):
    if n == 0:
        return 0
    lastDigit = n%10
    if lastDigit % 2 == 1:
        return removeOddDigits(n//10)
    else:
        return 10*removeOddDigits(n//10) + lastDigit

def onlyOddDigits(L):
    if L == []:
        return []
    return [removeOddDigits(L[0])] + onlyOddDigits(L[1:])
    