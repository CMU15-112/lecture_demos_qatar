import time
import ray

ray.init()

@ray.remote
class Node(object):

    def __init__(self, sublist):
        self.wordList= sublist

    def mostFrequentWordv1(self):
        maxword = None
        maxcnt = 0
        for word in self.wordList:
            cnt = self.wordList.count(word)
            if cnt > maxcnt:
                maxcnt = cnt
                maxword =word
        return (maxword, maxcnt)

    def freqWordsCount(self, mostFreqWords):
            d={}
            for w in mostFreqWords:
                    d[w]= self.wordList.count(w)
            return d

#l is a list of dicts
def finalMerge(l):
        finalD={}
        maxW=''
        for d in l:
                for w in d:
                        finalD[w]= finalD.get(w, 0)+d[w]
                        if maxW=='' or finalD[w] > finalD[maxW]:
                                maxW= w

        return maxW, finalD[maxW]   

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

nodes= []
sliceL= l//4

for i in range(0, l, sliceL):
    nodes.append(Node.remote(allWordsList[i:i+sliceL]))

futures1 = [nodes[i].mostFrequentWordv1.remote()  for i in range(4)]
initialResults= ray.get(futures1) # list of tuples .. each node returns a tuple of the most common word it has in its assigned sublist and the word count (mostCommonWord, wordCount)
mostCommonInAllNodes= set([t[0] for t in initialResults]) #this creates a set of all words that were most common in the sublists

# we now each counts the occurances of each common word in its sublist... and returns a dictionary where each entry is commonWord:commonWordCount
futures2 = [nodes[i].freqWordsCount.remote(mostCommonInAllNodes)  for i in range(4)]
finalResults= ray.get(futures2)

ans= finalMerge(finalResults) # applies a final merge for the returned dictionary
end = time.time()
elapsed1 = end - start
print("List-based\nAnswer {} in {:0.4f} seconds".format(ans, elapsed1))