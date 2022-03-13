import time
""" mostCommonWord: returns the most common word and its frequency"""

""" how many comparisons for alice_chap1.txt?
    2000 words
    2000 * 2000 = 4 Million

"""
def mostCommonWordv0(wordList):
    wordCount = {}
    maxcount = 0
    maxword = ""
    for word in wordList:
        count = wordList.count(word)
        if count > maxcount:
            maxcount = count
            maxword = word
    return (maxword, maxcount)

""" how many comparisons for alice_chap1.txt?
    depends on the number of unique words

"""

def mostCommonWordv1(wordList):
    wordCount = {}
    maxcount = 0
    maxword = ""
    for word in wordList:
        if word not in wordCount:
            wordCount[word] = wordList.count(word)
    (maxword, maxcount) = getMaxFromDict(wordCount)
    return (maxword, maxcount)

def getMaxFromDict(d):
    maxcount = 0
    maxword = ""
    for word in d:
        if d[word] > maxcount:
            maxcount = d[word]
            maxword = word
    return (maxword, maxcount)

""" how many comparisons for alice_chap1.txt?
    2000 words
    2000

"""
def mostCommonWordv2(wordList):
    wordCount = {}
    count = 0
    for word in wordList:
        if word not in wordCount:
            wordCount[word] = 0
        wordCount[word] += 1
    (maxword, maxcount) = getMaxFromDict(wordCount)
    return (maxword, maxcount)




    
def loadBook(filename):
    with open(filename,"r") as f:
        theText = f.read()
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":",'*']
    
    theText = theText.lower()
    
    for badChar in toRemove:
        theText = theText.replace(badChar," ")
    return theText.split()

#allWordsList = loadBook("alice_chap1.txt")
allWordsList = loadBook("alice.txt")
print(f"Loaded text with {len(allWordsList)} words")

start = time.time()
ans = mostCommonWordv0(allWordsList)
end = time.time()
elapsed1 = end - start
print("List-based\nAnswer {} in {:0.4f} seconds".format(ans,elapsed1))

start = time.time()
ans = mostCommonWordv1(allWordsList)
end = time.time()
elapsed1 = end - start
print("Dict-based with count\nAnswer {} in {:0.4f} seconds".format(ans,elapsed1))

start = time.time()
ans = mostCommonWordv2(allWordsList)
end = time.time()
elapsed1 = end - start
print("Dict-based WITHOUT count\nAnswer {} in {:0.4f} seconds".format(ans,elapsed1))