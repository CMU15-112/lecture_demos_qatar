def onlyVowels(s):
    if len(s) == 0:
        return ""
    else:
        othervowels = onlyVowels(s[1:])
        if s[0] in "aeiou":
            return s[0] + othervowels
        else:
            return othervowels
        
assert(onlyVowels("hello") == "eo")
assert(onlyVowels("bcdfg") == "")
assert(onlyVowels("aaaaa") == "aaaaa")