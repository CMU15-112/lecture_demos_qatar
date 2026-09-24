def isNearWord(word, target):
    # Delete a single letter from target and make it match word
    if len(target) == len(word) + 1:
        for i in range(len(target)):
            smallWord = target[:i] + target[i+1:]
            if smallWord == word:
                return True
    # Change one letter in target
    elif len(target) == len(word):
        mismatch = 0
        for i in range(len(target)):
            if target[i] != word[i]:
                mismatch += 1
        if mismatch == 1:
            return True
    # Add a letter to target so that it matches word
    elif len(target) + 1 == len(word):
        for i in range(len(word)):
            smallWord = word[:i] + word[i+1:]
            if smallWord == target:
                return True
    
    return False
    

# Takes a sorted list of lowercase words wordList and a single lowercase word.
# If the word is in wordList, then that word is returned.
# Otherwise, the function returns a list of all the words (in order) in
# wordList that can be obtained by making a single small edit on the given word.
# Small Edits are...
# - Deleting a single letter
# - Changing a single letter.
# - Adding a single letter
# If no such words exist, the function returns None.
def nearestWords(wordList, target):
    if target in wordList:
        return target
    
    res = []
    for word in wordList:
        if isNearWord(word, target):
            res.append(word)
            
    if len(res) == 0:
        return None
            
    return res
        
def testNearestWords():
    wordList = ['hi', 'i', 'love', 'watermelons']
    assert(nearestWords(wordList, 'ii') == ['hi', 'i'])
    assert(nearestWords(wordList, 'live') == ['love'])
    assert(nearestWords(wordList, 'hi') == 'hi')
    assert(nearestWords(wordList, 'watermelon') == ['watermelons'])
    assert(nearestWords(wordList, 'strawberry') == None)
    assert(nearestWords(wordList, '') == ['i'])
    assert(nearestWords([], '') == None)

def main():
    testNearestWords()

main()