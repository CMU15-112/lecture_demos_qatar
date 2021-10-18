def reverseString(s):
    r = ""
    for c in s:
        r = c + r
    return r

print(reverseString("abcdefgh"))

def reverseStringRec(s):
    # Base case
    if len(s) == 0:
        return ""
    
    # Recursive case
    return s[-1] + reverseStringRec(s[:-1])

print(reverseStringRec("abcdefgh"))

def reverseDandC(s):
    # Base case
    if len(s) == 0:
        return ""
    #elif len(s) == 1:
    #    return s
    
    # Recursive case with divide and conquer
    splitPoint = len(s)//2
    return reverseDandC(s[splitPoint:]) + reverseDandC(s[:splitPoint])

print(reverseDandC("abcdefgh"))