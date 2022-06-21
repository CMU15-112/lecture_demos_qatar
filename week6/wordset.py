class WordSet:
    def __init__(self):
        self.N = 1000037 
        self.buckets = [[]]*self.N 
    
    def myhash(self, word):
        return hash(word)
        """
        value = 0
        for c in word:
            value += ord(c)
        return value
        """
            
    def addWord(self, word):
        if self.find(word):
            return
        bucketForWord = self.myhash(word) % self.N
        if self.buckets[bucketForWord] == []:
            self.buckets[bucketForWord] = [word]
        else:
            # there's a collision
            self.buckets[bucketForWord].append(word)
    def find(self, word):
        bucketForWord = self.myhash(word) % self.N
        wordsInBucket = self.buckets[bucketForWord]
        if word in wordsInBucket:
            return True
        return False
    
    def stats(self):
        maxSize = 0
        totSize = 0
        emptyBuckets = 0
        for bucket in self.buckets:
            maxSize = max(maxSize, len(bucket))
            if len(bucket) == 0:
                emptyBuckets += 1
            totSize += len(bucket)
        print(f"Number of Buckets: {self.N}")
        print(f"Non-empty Buckets: {self.N - emptyBuckets}")
        print(f"Empty Buckets: {emptyBuckets}")
        print(f"Max. Size of Bucket: {maxSize}")
        print(f"Mean Size of Non-empty Bucket: {totSize / (self.N - emptyBuckets)}")
            
def load50KWords():
    words = []
    f = open("words.txt")
    for line in f.readlines():
        word = line.strip()
        words.append(word.lower())
    return words
    
def loadBook(filename):
    with open(filename,"r") as f:
        theText = f.read()
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":",'*']
    
    theText = theText.lower()
    
    for badChar in toRemove:
        theText = theText.replace(badChar," ")
    return theText.split()


def findInList(L, w):
    for word in L:
        if word == w:
            return True
    return False

def testList():
    print("Testing findInList")
    import random
    import time
    wordList =  load50KWords()
    wordsToFind = loadBook("alice.txt")
    print(f"Loaded book with {len(wordsToFind)} words")
    startTime = time.time()
    counter = 0
    for word in wordsToFind:
        if findInList(wordList, word):
            counter += 1
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Found %d words. time=%6.3fs" % (counter, elapsedTime))

def testWordSet():
    print("Testing find with WordSet")
    import random
    import time
    wordList =  load50KWords()
    wordsToFind = loadBook("alice.txt")
    print(f"Loaded book with {len(wordsToFind)} words")
    wordSet = WordSet()
    for word in wordList:
        wordSet.addWord(word)
        
    startTime = time.time()
    counter = 0
    for word in wordsToFind:
        if wordSet.find(word):
            counter += 1
    endTime = time.time()
    elapsedTime = endTime - startTime
    print("Found %d words. time=%6.3fs" % (counter, elapsedTime))
    wordSet.stats()


#testList()
testWordSet()

