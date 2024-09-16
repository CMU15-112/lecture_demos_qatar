# Return the number of vowels in s.
def vowelCount(s):
    count = 0
    s = s.lower()
    for c in s:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    return count

def vowelCount(s):
    vowels = "aeiouAEIOU"
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count

def vowelCount(s):
    count = 0
    vowels = "aeiouAEIOU"
    for c in vowels:
        count += s.count(c)
    return count

def vowelCount(s):
    initialOneCount = s.count('1')
    vowels = "aeiouAEIOU"
    for c in vowels:
        s = s.replace(c,'1')
    return s.count('1') - initialOneCount

def vowelCount(s):
    vowels = "aeiouAEIOU"
    for c in s:
        if c not in vowels:
            s = s.replace(c,"")
    return len(s)

def vowelCount(s):
    originalLength = len(s)
    vowels = "aeiouAEIOU"
    for c in vowels:
        s = s.replace(c,"")
    return originalLength - len(s)

#print(vowelCount('Abc def!!! a? yzyzyz123!'))

# Return the sum of all of the integers found in s
def numberSum(s):
    newS = ""
    for c in s:
        if c.isdigit():
            newS += c
        else:
            newS += " "
    res = 0
    for token in newS.split(" "):
        if token.isdigit():
           res += int(token)
    return res

def numberSum(s):
    res = 0
    memory = ""
    for c in s:
        if c.isdigit():
            memory += c
        elif memory != "":
                res += int(memory)
                memory = ""
    if memory != "":
        res += int(memory)
    return res

# What should this print? 92
print("Testing numberSum...", end="")
assert numberSum("I have 21 cats, 41 dogs, and 30 birds") == 92
assert numberSum("Ihave21cats,41dogs,and30birds") == 92
assert numberSum("21cats,41dogs,and30birds") == 92
assert numberSum("Ihave21cats,41dogs,andthebirdsare30") == 92
assert numberSum("Ihave21cats,41dogs,and-30birds") == 92
assert numberSum("Ihave21.41dogs,and-30birds") == 92
print("done")

# Return the frequency of the least frequently occuring letter in s
def leastFrequentCount(s):
    minimum = len(s)
    for c in s:
        if s.count(c) < minimum:
            minimum = s.count(c)
    return minimum

# Return which letters in s occur with frequency f
def lettersWithFreq(s, f):
    res = ""
    for c in s:
        if c not in res and s.count(c) == f:
            res += c
    return res[::-1]

# Given a string s, and ignoring case, return a lowercase string containing
# the least frequent alphabetic letters that occur in s.
def leastFrequentLetters(s):
    s = s.lower()
    
    newS = ""
    for c in s:
        if c.isalpha():
            newS += c
            
    # How many times does the least occurring letter occur?
    lowF = leastFrequentCount(newS)
    
    # Return which letters occur lowF times in newS
    result = lettersWithFreq(newS, lowF)
    
    return result

assert leastFrequentLetters("aDq efQ? FB'daf!!!") == "be"
