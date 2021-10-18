""" mostCommonWord: returns the most common word and its frequency"""  
def mostCommonWord(text):
    wordList = text.split(" ")
    wordCount = {}
    count = 0
    for word in wordList:
        if word not in wordCount:
            wordCount[word] = 0
        wordCount[word] += 1
    print(wordCount)

mostCommonWord("one two two three one one")

#assert(mostCommonWord("one two two three one one") == ("one", 3))
