def numberSum(s):
    """
    Return a sum of all of the positive integers in a string.
    Example:
    If s is... "I have 21 cats,41dogs, and 30 birds"
    then this will return 92.
    """
    
    sumDigits = 0
    memory = ""
    
    for c in s:
        if c.isdigit():
            memory+= c
        else:
            if memory != "":
                sumDigits += int(memory)
                memory = ""
            
    if memory != "":
        sumDigits+= int(memory)
            
    return sumDigits
    
 
 
def numberSumV2(s):
    numSum = 0
    i = 0

    while i < len(s):
        if s[i].isdigit():
            buffer = ""
            while i < len(s) and s[i].isdigit():
                buffer += s[i]
                i += 1
            numSum += int(buffer)
        else:
            i += 1
            
    return numSum


print("Testing numberSum... ", end="")
assert numberSum("I have 21 cats,41dogs, and 30 birds") == 92
assert numberSum("Ihave21cats,41dogs,and30birds") == 92
assert numberSum("Ihave2.1cats,4.13dogs,and30birds") == 50
assert numberSum("") == 0
assert numberSum("21 21") == 42
assert numberSum("Hello") == 0
assert numberSum("88Ihave21cats,41dogs,and30birds10") == 190
print("Done")