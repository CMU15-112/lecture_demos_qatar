import datetime

def loadBook(filename):
    # Load in the entire book as a single string, then make it lowercase
    with open(filename,"r") as f:
        theText = f.read()
    theText = theText.lower()

    # Remove punctuation and special characters
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":","*"]
    for badChar in toRemove:
        theText = theText.replace(badChar," ")
        
    return theText.split()

"""
Total work for 1000 word list:
1000 * 1000 = 1,000,000 steps
10000 * 10000 = 100,000,000 steps
"""
def mostCommonWord(wordList):
    maxCount = 0
    maxWord = ""
    for word in wordList:
        count = wordList.count(word)
        if count > maxCount:
            maxCount = count
            maxWord = word
    return (maxWord, maxCount)

"""
For 1000 words...
1000 * number of unique words
"""
def mostCommonWordv1(wordList):
    uniqueWords = set()
    maxCount = 0
    maxWord = ""
    for word in wordList:
        if word not in uniqueWords:
            uniqueWords.add(word)
            count = wordList.count(word)
            if count > maxCount:
                maxCount = count
                maxWord = word
    return (maxWord, maxCount)

"""
For 1000 word list...
1000
"""
def mostCommonWordv2(wordList):
    wordCount = dict()
    maxCount = 0
    maxWord = ""
    for word in wordList:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
            
        if wordCount[word] > maxCount:
            maxCount = wordCount[word]
            maxWord = word
            
    return (maxWord, maxCount)
        
    

files = ["alice_chap1.txt", "alice.txt", "donquixote.txt"]

for file in files:
    print(f"\n=== {file} ===")
    wordList = loadBook(file)

    print("Dictionary approach... ", end="")
    start = datetime.datetime.now()
    ans = mostCommonWordv2(wordList)
    end = datetime.datetime.now()
    print(f"done. Answer {ans} in {end-start} seconds")

    print("Set approach using count... ", end="")
    start = datetime.datetime.now()
    ans = mostCommonWordv1(wordList)
    end = datetime.datetime.now()
    print(f"done. Answer {ans} in {end-start} seconds")

    print("List approach using count... ", end="")
    start = datetime.datetime.now()
    ans = mostCommonWord(wordList)
    end = datetime.datetime.now()
    print(f"done. Answer {ans} in {end-start} seconds")
