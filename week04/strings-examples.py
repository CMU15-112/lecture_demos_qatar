# Interleave strings s1 and s2, returning the results.
# For example...
# s1 = "abc" and s2="def"
# then the return will be
# "adbecf"
def interleave(s1, s2):
    result = ""
    
    if len(s1) < len(s2):
        smallestStrLen = len(s1)
    else:
        smallestStrLen = len(s2)
    
    for i in range(smallestStrLen):
        print("i=", i)
        result += s1[i]
        result += s2[i]
    
    if len(s1) > len(s2):
        result += s1[i+1:]
    elif len(s2) > len(s1):
        result += s2[i+1:]
        
    return result

print(interleave("abc","123"))
print(interleave("abcdef","123"))
print(interleave("123","abcdef"))