def findLeastFreqCount(s):
    
    leastCount = len(s)
    
    for c in s:
        count = s.count(c)
        leastCount= min(count, leastCount)
        
    return leastCount

def lettersWithFreq(s, leastCount):
    
    result = ""
    
    for c in "abcdefghijklmnopqrstuvwxyz":
        if s.count(c) == leastCount:
            result+=c
            
    return result
            


def leastFrequentLetters(s):
    
    s = s.lower()
    
    newS = ""
    # remove non letters
    for c in s:
        if c.isalpha():
            newS+=c
            
    # find count of least frequent letter
    leastFreqCount = findLeastFreqCount(s)
    
    # find all least frequest letters that have the same count
    result = lettersWithFreq(s, leastFreqCount)
            
    return result

print(leastFrequentLetters("aDq efQ? FB'daf!!!")) #be
