def onlyVowels(s):
    if s == "":
        return ""
    else:
        smallS = s[0]
        partialAnswer = s[1:]
        return smallS if smallS in "aeiou" else "" + onlyVowels(PartialAnswer)
