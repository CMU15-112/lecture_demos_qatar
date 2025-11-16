def getAlpha(s):
    if s == "":
        return s
    if s[0].isalpha():
        return s[0] + getAlpha(s[1:])
    else:
        return getAlpha(s[1:])
    
def getNonAlpha(s):
    if s == "":
        return s
    if not s[0].isalpha():
        return s[0] + getNonAlpha(s[1:])
    else:
        return getNonAlpha(s[1:])


    
def recRearrangeLettersInFrontv1(s):
    s1 = getAlpha(s)
    s2 = getNonAlpha(s)
    return s1 + s2

def recRearrangeLettersInFrontv2(s, s1="", s2=""):
    if s == "":
        return s1 + s2
    if s[0].isalpha():
        return recRearrangeLettersInFront(s[1:], s1+s[0], s2)
    if not s[0].isalpha():
        return recRearrangeLettersInFront(s[1:],s1, s[0]+s2)    

    