import time

# Here we use a dictionary to keep the count of the elements
# Note that we go through the list once and, incrementally, build
# a dictionary that maps words to frequency
# At the same time, we keep track of the word with highest frequency
# But we could also find the most frequent word from the dictionary in a second loop after
# building the dictionary

def mostFrequentWordv3(wordList):
    maxword = None
    maxcnt = 0
    wordFreq = {}
    for word in wordList:  # n times
        if word not in wordFreq:  # o(1)
            wordFreq[word] = 1  #o(1)
        else:
            wordFreq[word]+=1 # O(1)
        # wordFreq has a key word
        if wordFreq[word] > maxcnt:
            maxcnt = wordFreq[word] #O(1)
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

allWordsList = loadBook("shakespeare.txt")
print(f"Loaded text with {len(allWordsList)} words")

start = time.time()
ans = mostFrequentWordv3(allWordsList)
end = time.time()
elapsed1 = end - start
print("Dict-based\nAnswer {} in {:0.4f} seconds".format(ans, elapsed1))
