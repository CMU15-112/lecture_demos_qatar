# Tail recursion

def onlyVowelsHelper(s, currentVowels):
    if len(s) == 0:
        return currentVowels
    if s[0] in 'aeiou':
        currentVowels += s[0]
    return onlyVowelsHelper(s[1:], currentVowels)

def onlyVowels(s):
    return onlyVowelsHelper(s, "")
    
    
assert(onlyVowels("hello") == "eo")
assert(onlyVowels("bcdfg") == "")
assert(onlyVowels("aaaaa") == "aaaaa")
