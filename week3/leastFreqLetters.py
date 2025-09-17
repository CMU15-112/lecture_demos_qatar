def leastFrequentLetters(s):
    # remove non-alphabetic
    # letters?
    # Find lowest freq
    lowerS = s.lower()
    minCount = len(s)+1
    if s == "":
        return ""
    for c in lowerS:
        if c.isalpha():
            # we have to check the frequency of its lowercase counterpart
            # using the lowercase string
            cnt = lowerS.count(c)
            if cnt < minCount:
                minCount = cnt
    result = ""
    # keep lowest freq
    for c in s:
        #  check only alphabetical
        if c.isalpha():
            # we have to check the frequency of its lowercase counterpart
            # using the lowercase string
            cnt = lowerS.count(c.lower())
            if cnt == minCount:
                result += c
    return result


assert leastFrequentLetters("aaaBbcc") == "Bbcc"
assert leastFrequentLetters("aAbB") == "aAbB"
assert leastFrequentLetters("aAbBC") == "C"
assert leastFrequentLetters("") == ""
print("passed.")