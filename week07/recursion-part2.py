def reverse(s):
    r = ""
    for c in s:
        r = c + r
    return r

# Approach 1: "Standard" Recursion

def reverseStandard(s):
    if len(s) == 1:
        return s
    #return reverseStandard(s[1:]) + s[0]
    return s[-1] + reverseStandard(s[:-1])

print(reverseStandard("abcdefghijklmnopqrstuvwxyz"))

# Approach 2: Divide and Conquer

def reverseDC(s):
    if len(s) == 1:
        return s    
    midPoint = len(s)//2
    return reverseDC(s[midPoint:]) + reverseDC(s[:midPoint])

print(reverseDC("abcdefghijklmnopqrstuvwxyz"))