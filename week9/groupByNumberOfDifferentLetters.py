# Given a list of words, return a dictionary that groups words by the number of different characters occurring in the word
# the keys will be the number of different letters.
# For a certain key n, the value is a set that contains all words in L that feature n different characters
# For instance, groupByNumberOfDifferentLetters(['supply', 'seller', 'cotton']) returns the dictionary
# {4: {'cotton', 'seller'}, 5: {'supply'} }


def numberOfUniqueLetters(s):
    myset = set()
    for c in s:
        myset.add(c)
    return len(myset)
    
# numberOfUniqueLetter("seller") == 5

def groupByNumberOfDifferentLetters(L):
    d = dict()
    for w in L:
        num = numberOfUniqueLetters(w)        
        if num in d:
            d[num].add(w)
        else:
            d[num] = {w}
    return d

# def groupByNumberOfDifferentLetters(L):
#     d = dict()
#     for w in L:
#         num = numberOfUniqueLetters(w)        
#         if num not in d:
#             d[num]={}
#         d[num].add(w)
#     return d


def testGroupByNumberOfDifferentLetters():
    L = ['artist', 
         'supply', 
         'seller', 
         'cotton', 
         'subway', 
         'tablet', 
         'pepper', 
         'freeze']
    assert( groupByNumberOfDifferentLetters(L) == {3: {'pepper'},
                                                   4: {'cotton', 'freeze', 'seller'},
                                                   5: {'artist', 'supply', 'tablet'},
                                                   6: {'subway'}})
    print("passed.")
    
testGroupByNumberOfDifferentLetters()