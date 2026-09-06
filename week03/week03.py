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
    lowestFreq = frequencyOfLeastOccurringLetter(s)
    res = getLettersWithFrequency(s, freq)
    res = alphabetize(res)
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