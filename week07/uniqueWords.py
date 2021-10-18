def loadBook(filename):
    with open(filename,"r") as f:
        theText = f.read()
    """ theText whole text as string """
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":",'*']
    
    theText = theText.lower()
    
    for badChar in toRemove:
        theText = theText.replace(badChar," ")
    return theText


fulltext = loadBook("donquixote.txt")
print("Loaded text with {} words and {} characters".format(len(fulltext.split()), len(fulltext)))
wordList = fulltext.split()

wordSet = set(wordList)
print("Number of unique words: {}".format(len(wordSet)))



