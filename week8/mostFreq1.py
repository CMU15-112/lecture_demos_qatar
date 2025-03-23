import time

# N = len(wordList)
def mostFrequentWordv1(wordList):  # O(N^2)
    maxword = None  # O(1)
    maxcnt = 0  # O(1)
    for word in wordList:  # O(N) 
        cnt = wordList.count(word) # O(N)
        if cnt > maxcnt:  #O(1)
            maxcnt = cnt # O(1)
            maxword =word #O(1)
    return (maxword, maxcnt)  #O(1)

""" let's use a list to avoid counting twice the
same words  """
def mostFrequentWordv2(wordList):
    # assume n = len(wordList)
    # assume m = number of unique words
    maxcnt = -1
    maxword = ""
    countedWords = []
    for word in wordList:
        if word in countedWords: # performs m checks
            continue
        cnt = wordList.count(word)  # performs m checks
        countedWords.append(word)
        if cnt > maxcnt:
            maxcnt = cnt
            maxword = word
    return maxword, maxcnt

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
print("List-based\nAnswer {} in {:0.4f} seconds".format(ans, elapsed1))
