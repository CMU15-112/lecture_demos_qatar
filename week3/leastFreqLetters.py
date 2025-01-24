def leastFrequentLetters(s):
    # remove non-alphabetic
    # letters?
    # Find lowest freq
    lowerS = s.lower()
    minCount = len(s)+1
    for c in lowerS:
        if c.isalpha():
            cnt = lowerS.count(c)
            if cnt < minCount:
                minCount = cnt
    result = ""
    # keep lowest freq
     for c in s:
        if c.isalpha():
            cnt = lowerS.count(c.lower())
            if cnt < minCount:
                minCount = cnt
    