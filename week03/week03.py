# Returns the number of vowels in s
def vowelCount(s):
    res = 0
    for c in s.lower():
        if c in "aeiou":
            res += 1
    return res

# Return the sum all the numbers in string s
# For example...
# "I have 21 cats, 41 dogs, and 30 birds" returns 92.
def numberSum(s):
    res = 0
    i = 0
    while i < len(s):
        curNum = ""
        if s[i].isdigit():
            for j in range(i, len(s)):
                if s[j].isdigit():
                    curNum += s[j]
                else:
                    break
            print(f"curnum is {curNum}")
            res += int(curNum)
            i = j - 1
        i += 1
    return res

assert numberSum("I have 21cats, 41 dogs, and 30 birds") == 92
print("---")
def numberSumAgain(s):
    res = 0
    memory = ""
    for c in s:
        if c.isdigit():
            memory += c
        elif memory != "":
            print(f"memory {memory}")
            res += int(memory)
            memory = ""
    # What if the memory isn't empty when the string ends?
    if memory != "":
        res += int(memory)
    return res

assert numberSumAgain("I have 21cats, 41 dogs, and 30 birds7") == 99

print("---")

# Least frequent letters
# Return the least frequently occuring letters in the string
# Example:
# leastFrequentLetters("aDq efQ? FB'daf!!!") == 'be'
def leastFrequentLetters(s):    
    s = removeNonLettersAndMakeLower(s)
    
    # Empty strings have no least frequent character
    if s == "":
        return ""
    
    lowestFreq = frequencyOfLeastOccurringLetter(s)
    res = getLettersWithFrequency(s, lowestFreq)
    #res = alphabetize(res)
    return res

def removeNonLettersAndMakeLower(s):
    res = ""
    for c in s:
        if c.isalpha():
            res += c
    return res.lower()

assert removeNonLettersAndMakeLower("aDq efQ? FB'daf!!!") == "adqefqfbdaf"

def frequencyOfLeastOccurringLetter(s):
    lowestFreq = len(s)
    for letter in "abcdefghijklmnopqrstuvwxyz":
        cnt = s.count(letter)
        if cnt != 0 and cnt < lowestFreq:
            lowestFreq = cnt
    return lowestFreq

assert frequencyOfLeastOccurringLetter("adqefqfbdaf") == 1
assert frequencyOfLeastOccurringLetter("adqfqfdaf") == 2

def getLettersWithFrequency(s, freq):
    res = ""
    for letter in "abcdefghijklmnopqrstuvwxyz":
        cnt = s.count(letter)
        if cnt == freq:
            res += letter
    return res

assert getLettersWithFrequency("adqefqfbdaf", 1) == "be"
assert getLettersWithFrequency("adqefqfbdaf", 2) == "adq"
assert getLettersWithFrequency("adqefqfbdaf", 3) == "f"
assert getLettersWithFrequency("adqefqfbdaf", 4) == ""


assert leastFrequentLetters("aDq efQ? FB'daf!!!") == "be"
assert leastFrequentLetters("") == ""
assert leastFrequentLetters("1234") == ""



print("---")

# Anagrams are strings containing the same letters, but in a potentially
# different order
# Not case sensitive.  Only consider non-space characters
# Example: "dormitory", "Dir   tyr oo m"
def areAnagrams(s1, s2):
    
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    
    if len(s1) != len(s2):
        return False
    
    for c in s1:
        if s1.count(c) != s2.count(c):
            return False
    return True

assert areAnagrams("dormitory","dirtyroom") == True
assert areAnagrams("dormitory","dirtyrom") == False
assert areAnagrams("dormitory","dirtyrorm") == False
assert areAnagrams("dormitory","Dirtyroom") == True
assert areAnagrams("dorm      itory","di rtyr  oom") == True
assert areAnagrams("12345!@.","12345!@.") == True
assert areAnagrams("12345!@.3","1345!@.23") == True
assert areAnagrams(123, 123) == 






print("done")