def mostCommonWord(L):
    commonWord = ""
    numTimes = 0
    
    for word in L:
        cnt = L.count(word)
        if cnt > numTimes:
            numTimes = cnt
            commonWord = word
    
    return (commonWord, numTimes)

def mostCommonWordFaster(L):
    
    wordDictionary = dict()
    for word in L:  #O(N)
        if word in wordDictionary:
            wordDictionary[word] += 1
        else:
            wordDictionary[word] = 1
            
    commonWord = ""
    numTimes = 0
    
    for word in wordDictionary: #O(N)
        cnt = wordDictionary[word]
        if cnt > numTimes:
            numTimes = cnt
            commonWord = word
    
    return (commonWord, numTimes)
text = """Either the well was very deep, or she fell very slowly, for she had
plenty of time as she went down to look about her and to wonder what was
going to happen next. First, she tried to look down and make out what
she was coming to, but it was too dark to see anything; then she
looked at the sides of the well, and noticed that they were filled with
cupboards and book-shelves; here and there she saw maps and pictures
hung upon pegs. She took down a jar from one of the shelves as
she passed; it was labelled 'ORANGE MARMALADE', but to her great
disappointment it was empty: she did not like to drop the jar for fear
of killing somebody, so managed to put it into one of the cupboards as
she fell past it."""

newText = ""
for c in text:
    if c.isalpha() or c.isspace():
        newText += c
        
words = newText.lower().split()
print(mostCommonWord(words))

with open("alice.txt","r") as f:
    text = f.read()
    newText = ""
    for c in text:
        if c.isalpha() or c.isspace():
            newText += c
            
    words = newText.lower().split()
    print(mostCommonWordFaster(words))
