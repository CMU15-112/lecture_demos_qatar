# Write a recursive function that returns a string containing only the vowels occurring in s
# in the same order
# onlyVowels("hello") == "eo"
# onlyVowels("bcdfg") == ""
# onlyVowels("aaaaa") == "aaaaa"

def onlyVowels(s):
    if s == "":
        return ""
    else:
        if s[0].lower() in "aeiou":
            result = s[0] + onlyVowels(s[1:])
            return result
        else:
            result = onlyVowels(s[1:])
            return result

def testOnlyVowels():
    print("Testing onlyVowels...", end="")
    assert(onlyVowels("hello") == "eo")
    assert(onlyVowels("bcdfg") == "")
    assert(onlyVowels("aaaaa") == "aaaaa")
    print("passed!")
    
testOnlyVowels()