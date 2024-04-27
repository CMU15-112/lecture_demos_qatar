import time

def mostFrequentWordv1(wordList):
    maxword = None
    maxcnt = 0
    for word in wordList:
        cnt = wordList.count(word)
        if cnt > maxcnt:
            maxcnt = cnt
            maxword =word
    return (maxword, maxcnt)


def loadBook(filename):
    with open(filename,"r", encoding='utf-8') as f:
        theText = f.read()
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":",'*']

    theText = theText.lower()

    for badChar in toRemove:
        theText = theText.replace(badChar," ")
    return theText.split()

allWordsList = loadBook("alice.txt")
print(f"Loaded text with {len(allWordsList)} words")

start = time.time()
ans = mostFrequentWordv1(allWordsList)
end = time.time()
elapsed1 = end - start
print("List-based\nAnswer {} in {:0.4f} seconds".format(ans, elapsed1))

print("Time: ", elapsed1)
