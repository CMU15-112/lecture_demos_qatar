def leastFrequentLetters(s):
    # filter non-alpha characters
    news = ""
    for c in s:
        if c.isalpha():
            news += c
    news = news.lower()

    # find minimun frequency
    countList = []
    for c in news:
        countList.append(news.count(c))
    
    minFreq = min(countList)    
    leastFreqLetters = ""
    for c in news:
        if news.count(c) == minFreq:
            leastFreqLetters += c
    
    sortedListChar = sorted(leastFreqLetters)
    res = ""
    for c in sortedListChar:
        res += c

    return res
    
            

leastFrequentLetters("aDq efQ? FB'daf!!!") 
    
    
    
        
    