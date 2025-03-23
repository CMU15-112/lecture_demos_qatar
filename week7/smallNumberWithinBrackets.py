def getNumber(ns):
    if ns[0] == '-' and ns[1:].isdigit():
        return int(ns)
    elif ns.isdigit():
        return int(ns)
    else:
        return None
    
    
def smallestNumberWithinBrackets(s):
    res = math.inf # no numbers so far
    for i in range(len(s)): # check each character
        if s[i] == '[': # found [
            # find next ]
            for j in range(i+1, len(s)):
                if s[j] == ']':
                    numstr = s[i+1:j]
                    num = getNumber(numstr)
                    if num != None:
                        if res == None:
                            res = num
                        else:
                            res = min(res, num)
                    else:
                        break
    return res
                            