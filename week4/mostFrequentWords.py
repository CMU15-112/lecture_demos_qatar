import time

""" returns the most frequent word together with its frequency """

""" assume len(wordList)= 2000 """
""" 2000 x 2000 """

def mostCommonWordv0(wordList):
    maxcnt = -1
    maxword = ""
    for word in wordList:
        cnt = wordList.count(word)
        if cnt > maxcnt:
            maxcnt = cnt
            maxword = word
    return maxword, maxcnt

""" let's use a dictionary to avoid counting twice the
same words  """
def mostCommonWordv1(wordList):
    maxcnt = -1
    maxword = ""
    countedWords = {}
    for word in wordList:
        if word in countedWords:
            continue
        cnt = wordList.count(word)
        countedWords[word] = cnt
        if cnt > maxcnt:
            maxcnt = cnt
            maxword = word
    return maxword, maxcnt

def getMaxFromDict(d):  # return (key, val) with greatest val
    maxval = 0
    maxword = None
    for key, val in d.items():
        if val > maxval:
            maxval = val
            maxword = key
    return maxword, maxval
        
    
def mostCommonWordv2(wordList):
    maxcnt = -1
    maxword = ""
    countedWords = {}
    for word in wordList:
        countedWords[word] = countedWords.get(word, 0) + 1
    return getMaxFromDict(countedWords)
    
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
    
 
    