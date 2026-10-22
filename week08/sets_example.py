import datetime

### Return all of the unique words in the text

# Using lists
def uniqueWordsLists(words):
    uniqueWords = []
    for word in words:
        if word not in uniqueWords:
            uniqueWords.append(word)

    return uniqueWords

def uniqueWordsSets(words):
    uniqueWords = set(words)

    return uniqueWords

### Use this to count the unique words in a book

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

files = ["alice_chap1.txt", "alice.txt", "donquixote.txt"]

for file in files:
    print(f"\n=== {file} ===")
    
    wordList = loadBook(file)

    print("Getting the unique words using sets... ", end="")
    start = datetime.datetime.now()
    wordList = uniqueWordsSets(wordList)
    end = datetime.datetime.now()
    print(f"done ({len(wordList)} words) ({end-start})")

    print("Getting the unique words using lists... ", end="")
    start = datetime.datetime.now()
    wordList = uniqueWordsLists(wordList)
    end = datetime.datetime.now()
    print(f"done ({len(wordList)} words) ({end-start})")