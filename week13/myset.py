



class WordSet:
    def __init__(self):
        self.N = 1000037 
        self.buckets = []
        for i in range(self.N):
            self.buckets.append([])
        self.numberOfWords = 0
# we could use our own hash            
#     def myhash(self, s):
#         total = 1
#         for c in s:
#             total *= ord(c)       
#         return total%self.N
# but instead let's use Python's built-in hash
    def myhash(self, s): 
        return hash(s)%self.N
    
    def length(self):
        return self.numberOfWords
         
    def addWord(self, word):
        bucketIndex = self.myhash(word) % self.N
        bucketForWord = self.buckets[bucketIndex]
        if word not in bucketForWord:
            bucketForWord.append(word)
            self.numberOfWords += 1
        
    def find(self, word):
        bucketIndex = self.myhash(word) % self.N
        wordBucket = self.buckets[bucketIndex]
        if word in wordBucket:
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
      
        
testWordSet()  
        
        
        
            
    