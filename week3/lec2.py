# still doesn't handle negative d
def convertUpperLetter(c, d):
    n = ord(c)
    n += d
    if n > ord("Z"):
        n -= 26
    elif n < ord("A"):
        n += 26
    return chr(n)
    
def convertLowerLetter(c, d):
    n = ord(c)
    n += d
    if n > ord("z"):
        n -= 26
    elif n < ord("a"):
        n += 26
    return chr(n)
    
#def convertUpperLetter(c, d):
#    n = ord(c)-ord("A")
#    n = (n+d)%26
#    n += ord("A")
#    return chr(n)

def encodeOffset(s, d):
    res = ""
    
    for c in s:
        if c.isupper():
            res += convertUpperLetter(c, d)
        elif c.islower():
            res  += convertLowerLetter(c,d)
        else:
            res += c
    
    return res