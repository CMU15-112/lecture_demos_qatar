import time

# Trying to "optimize" by avoiding counting the word twice
# It won't make a difference if there aren't many repeated words
def mostFrequentWordv2(wordList):
    maxword = None
    maxcnt = 0
    countedList = []
    for word in wordList:
        if word in countedList:
            continue
        cnt = wordList.count(word)
        if cnt > maxcnt:
            maxcnt = cnt
            maxword =word
        countedList.append(word)
    return (maxword, maxcnt)

def loadBook(filename):
    with open(filename,"r", encoding='utf-8') as f:
        theText = f.read()
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":",'*']

    theText = theText.lower()

    for badChar in toRemove:
        theText = theText.replace(badChar," ")
    return theText.split()

allWordsList = loadBook("shakespeare.txt")
print(f"Loaded text with {len(allWordsList)} words")

start = time.time()
ans = mostFrequentWordv2(allWordsList)
end = time.time()
elapsed1 = end - start
print("Yet another List-based\nAnswer {} in {:0.4f} seconds".format(ans, elapsed1))
