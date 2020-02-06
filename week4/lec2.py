# Do NOT assume both strings are the same length
def interleave(s1, s2):
    res = ""
    
    x = max(len(s1),len(s2))
    
    for i in range(x):
        if i < len(s1):
            res += s1[i]
    
        if i < len(s2):
            res += s2[i]
            
    return res

def interleave(s1, s2):
    res = ""
    
    smaller = min(len(s1),len(s2))
    
    for i in range(smaller):
        res += s1[i]
        res += s2[i]
    
    if len(s1) > len(s2):
        res += s1[smaller:]
    else:
        res += s2[smaller:]
        
    return res

assert(interleave("abcxyz","def") == "adbecfxyz")
assert(interleave("abc","defxyz") == "adbecfxyz")

# Returns True is s1 and s2 contains the same characters (even if the # of characters is different)
# and False otherwise
# Examples:
#  sameChars("abc", "aabbcc") == True
#  sameChars("aBc", "cbAa") == True
#  sameChars("cat", "catalay") == False
def containsChars(s1, s2):
    for letter in s1:
        if letter not in s2:
            return False
    return True

def sameChars(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    # I need to check both ways
    return containsChars(s1,s2) and containsChars(s2,s1)

assert(sameChars("abc", "aabbcc") == True)
assert(sameChars("aBc", "cbAa") == True)
assert(sameChars("cat", "catalay") == False)

def containsCharsWithCount(s1, s2):
    for letter in s1:
        if s1.count(letter) != s2.count(letter):
            return False
    return True

def areAnagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    
    if len(s1) != len(s2):
        return False
    
    # I need to check both ways
    return containsCharsWithCount(s1,s2)# and containsCharsWithCount(s2,s1)

print(areAnagrams("dormitory","dirtyroom"))
print(areAnagrams("dormitory","dirtyromm"))
print(areAnagrams("",""))
print(areAnagrams("dormitory","dormitoryb"))

# Return the largest positive number found in the string
# You can assume - will not appears
# Example:
#   largestNumber("I have 21 cats, 41 dogs, and 30 birds") == 41

# Returns a list of the integers in s
# Example:
#    extractNumbers("I have 21 cats, 41 dogs, and 30 birds") == [21, 41, 30]
def extractNumbers(s):
    res = []
    memory = ""
    
    for letter in s:
        if letter.isdigit():
            memory += letter
        else:
            if len(memory) > 0:
                num = int(memory)
                res.append(num)
                memory = ""

    return res

print(extractNumbers("I have 21 cats, 41 dogs, and 30 birds"))

def largestNumber(text):
    numList = extractNumbers(text)
    return max(numList)