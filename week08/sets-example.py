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

    return theText

def uniqueWordsLists(words):
    uniqueWords = []
    for word in words:
        if word not in uniqueWords:
            uniqueWords.append(word)
    return uniqueWords

def uniqueWordsSets(words):
    return list(set(words))

theText = loadBook("donquixote.txt")
theWords = theText.split()

print("Getting the unique words using sets... ", end="")
start = datetime.datetime.now()
uniq = uniqueWordsSets(theWords)
end = datetime.datetime.now()
print(f"done. ({len(uniq)} {end-start})")

print("Getting the unique words using lists... ", end="")
start = datetime.datetime.now()
uniq = uniqueWordsLists(theWords)
end = datetime.datetime.now()
print(f"done. ({len(uniq)} {end-start})")
