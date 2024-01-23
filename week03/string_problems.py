def vowelCount(s):
    """
    Takes a string, s, and returns the number of vowels inside s.
    Ignore case, so A and a are both vowels.
    """
    vowels = "aeiouAEIOU"
    cnt = 0
    for c in s:
        if c in vowels:
            cnt += 1
    return cnt

print("Testing vowelCount... ", end="")
assert vowelCount("hello") == 2
assert vowelCount("hello mitochondria") == 7
assert vowelCount("hellO mitochondrIa") == 7
assert vowelCount("uhellO mitochondrIa") == 8
assert vowelCount("") == 0
print("done")

def numberSum(s):
    """
    Return a sum of all of the positive integers in a string.
    Example:
    If s is... "I have 21 cats,41dogs, and 30 birds"
    then this will return 92.
    """
    numSum = 0
    memory = ""
    for c in s:
        if c.isdigit():
            memory += c
        else:
            if memory != "":
                numSum += int(memory)
                memory = ""
    if memory != "":
        numSum += int(memory)
    return numSum
       
def numberSumAgain(s):
    numSum = 0
    
    i = 0
    while i < len(s):
        buffer = ""
        while i < len(s) and s[i].isdigit():
            buffer += s[i]
            i += 1
        if buffer != "":
            numSum += int(buffer)
            buffer = ""
        i += 1
    return numSum
       
print("Testing numberSum... ", end="")
assert numberSumAgain("I have 21 cats,41dogs, and 30 birds") == 92
assert numberSumAgain("Ihave21cats,41dogs,and30birds") == 92
assert numberSumAgain("Ihave2.1cats,4.13dogs,and30birds") == 50
assert numberSumAgain("") == 0
assert numberSumAgain("88Ihave21cats,41dogs,and30birds10") == 190
print("Done")

def leastFrequentCount(s):
    lowF = s.count(s[0])
    for c in s:
        freq = s.count(c)
        lowF = min(lowF, freq)
    return lowF

def lettersWithFreq(s, freq):
    result = ""
    for c in "abcdefghijklmnopqrstuvwxyz":
        if s.count(c) == freq:
            result += c
    return result
    
def leastFrequentLetters(s):
    # Make lowercase
    s = s.lower()
    # Remove non-letters
    newS = ""
    for c in s:
        if c.isalpha():
            newS += c
    # Find count of least frequent letter
    lowFreqCount = leastFrequentCount(newS)
    # Find letters with least frequent count
    result = lettersWithFreq(newS, lowFreqCount)
    
    return result

print(leastFrequentLetters("aDq efQ? FB'daf!!!"))