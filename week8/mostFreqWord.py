import time

def mostFrequentWordUgly(wordList):  
    maxword = None  
    maxcount = 0  
    for word in wordList:   
        cnt = wordList.count(word) 
        if cnt > maxcount: 
            maxcount = cnt 
            maxword =word 
    return (maxword, maxcount)

""" let's use a list to avoid counting twice the
same words  """
def mostFrequentWordBad(wordList):
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

# Here we use a dictionary to keep the count of the elements
# Note that we go through the list once and, incrementally, build
# a dictionary that maps words to frequency
# At the same time, we keep track of the word with highest frequency
# But we could also find the most frequent word from
# the dictionary in a second loop after building it

def mostFrequentWordGood(wordList):  
    maxword = None  
    maxcount = 0
    wordFreq = {} 
    for word in wordList:   
        if word not in wordFreq: 
            wordFreq[word] = 1  
        else:
            wordFreq[word] += 1 
        # now wordFreq has a 'word' as a key
        if wordFreq[word] > maxcount:  
            maxcount = wordFreq[word] 
            maxword =word
    return (maxword, maxcount)

def loadBook(filename):
    with open(filename,"r", encoding='utf-8') as f:
        theText = f.read()
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":",'*']
    theText = theText.lower()
    for badChar in toRemove:
        theText = theText.replace(badChar," ")
    return theText.split()

manyWords = loadBook("shakespeare.txt")
manyWords = manyWords[:10000] # use only 10K, ugly and bad won't handle all words


print(f"Testing one case with len(wordList) = {len(manyWords)} words")
print("-"*40)

start = time.time()
result = mostFrequentWordUgly(manyWords)
timeElapsed = time.time() - start
print(f'Ugly version returned "{result}" in {timeElapsed:0.4f} seconds')

start = time.time()
result = mostFrequentWordBad(manyWords)
timeElapsed = time.time() - start

print(f'"Bad" version returned "{result}" in {timeElapsed:0.4f} seconds')


start = time.time()
result = mostFrequentWordGood(manyWords)  
timeElapsed = time.time() - start

print(f'"Good" version returned "{result}" in {timeElapsed:0.4f} seconds')
