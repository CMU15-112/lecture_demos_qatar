def wordCounter(s):
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--",
                "]","[",":"]
    
    s = s.lower()
    
    for badChar in toRemove:
        s = s.replace(badChar," ")
    
    words = s.split()
    
    res = dict()
    
    for word in words:
        if word not in res:
            res[word] = 0
        res[word] += 1
        
    return res

# Return the most common word and the number of times it occurs
def mostCommonWord(s):
    d = wordCounter(s)
    
    biggestWord = ""
    biggestCount = 0
    
    for key in d:
        value = d[key]
        #print(key,value)
        if value > biggestCount:
            biggestCount = value
            biggestWord = key
            
    return (biggestWord, biggestCount)

def mostCommonWordSortHack(s):
    d = wordCounter(s)
    
    wordList = []
    for key in d:
        value = d[key]
        wordList.append( (value, key) )
            
    return sorted(wordList)

def mostCommonWordWithoutDictionaries(s):
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--",
                "]","[",":"]
    
    s = s.lower()
    
    for badChar in toRemove:
        s = s.replace(badChar," ")
    
    words = s.split()

    biggestWord = ""
    biggestCount = 0
    
    for word in words:
        count = words.count(word)
        if count > biggestCount:
            biggestCount = count
            biggestWord = word
    
    return biggestWord, biggestCount

text = """
'Well!' thought Alice to herself, 'after such a fall as this, I shall
think nothing of tumbling down stairs! How brave they'll all think me at
home! Why, I wouldn't say anything about it, even if I fell off the top
of the house!' (Which was very likely true.)"""

ans = mostCommonWord(text)
print(ans)
ans2 = mostCommonWordWithoutDictionaries(text)
print(ans2)

print("---")

with open("alice.txt","r") as f:
    aliceText = f.read()
    ans = mostCommonWord(aliceText)
    print(ans)
    ans2 = mostCommonWordWithoutDictionaries(aliceText)
    print(ans2)