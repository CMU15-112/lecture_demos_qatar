import time
import ray

ray.init()


#l is a list of dicts
def finalMerge(l):
        print("final merge: ", l)
        finalD={}
        maxW=''
        for d in l:
                for w in d:
                        finalD[w]= finalD.get(w, 0)+d[w]
                        if maxW=='' or finalD[w] > finalD[maxW]:
                                maxW= w

        return maxW, finalD[maxW]

@ray.remote
def mostFrequentWordv1(wordList):
    maxword = None
    maxcnt = 0
    for word in wordList:
        cnt = wordList.count(word)
        if cnt > maxcnt:
            maxcnt = cnt
            maxword =word
    return (maxword, maxcnt)


@ray.remote
def mostFreqAcrossNodes(mostFreqWords, wordList):
        d={}
        for w in mostFreqWords:
                d[w]= wordList.count(w)
        return d


def loadBook(filename):
    with open(filename,"r", encoding='utf-8') as f:
        theText = f.read()
    toRemove = [",",";",".","\"","\' ","\n\'"," \'","!","(",")","?","--","'",'"',"]","[",":",'*']

    theText = theText.lower()

    for badChar in toRemove:
        theText = theText.replace(badChar," ")
    return theText.split()

allWordsList = loadBook("alice.txt")
#allWordsList= [1,1,2,3,4,1,2,2,3,4,1,2,3,3,4,1,2,3,4,1]
print(f"Loaded text with {len(allWordsList)} words")

start = time.time()
l=  len(allWordsList)
sliceL= l//4

futures1 = [mostFrequentWordv1.remote(allWordsList[i:i+sliceL])  for i in range(0, l, sliceL)]

initialResults= ray.get(futures1) # list of tuples .. each node returns a tuple of the most common word it has in its assigned sublist and the word count (mostCommonWord, wordCount)
print('initialResults: ', initialResults)

mostCommonInAllNodes= set([t[0] for t in initialResults]) #this creates a set of all words that were most common in the sublists
print('initial Ans: ', mostCommonInAllNodes)

# we now each counts the occurances of each common word in its sublist... and returns a dictionary where each entry is commonWord:commonWordCount
futures2 = [mostFreqAcrossNodes.remote(mostCommonInAllNodes, allWordsList[i:i+sliceL])  for i in range(0, l, sliceL)]
finalResults= ray.get(futures2)

ans= finalMerge(finalResults) # applies a final merge for the returned dictionary 
print("Final res:", finalResults)
print("Final Ans: ", ans)
end = time.time()
elapsed1 = end - start
print("List-based\nAnswer {} in {:0.4f} seconds".format(ans, elapsed1))

print("Time: ", elapsed1)
