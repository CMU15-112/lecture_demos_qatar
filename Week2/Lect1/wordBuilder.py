'''
We say that a word, w1, can be used to build another word, w2,
if some subset of the letters from w1 can be rearranged to produce the word w2.
For example, the word "water" can be used to build "rate", "tear", "at", etc.
(But it can't be used to build "rater" because "water" only has one r, not two.)'''
def wordCanBeBuilt(s1, s2):
    for c in s2:
        if not s1.count(c) >= s2.count(c):
            return False
    return True

'''
Write the function canBuild(word, manyWords) that takes as arguments
a string containing a word and another string containing a comma-separated
list of words, and returns a comma-separated list of words from
manyWords that can be built from word. 
'''
def canBuild(word, manyWords):
    ret = ""
    for w in manyWords.split(","):
        if wordCanBeBuilt(word, w):
            if ret == "":
                ret = w
            else:
                ret += ","+w
    return ret


assert canBuild("damthewater", "ad,add,sad,mad,tear") == "ad,mad,tear"
assert canBuild("freakymonkeytips", "far,jet,pit,lip,jaw,sip") == "far,pit,sip"
bigWord = "supercalifragilisticexpialidocious"
bigList = "jet,pit,hero,sail,space,lack,pride,tile,park,drug,steam"
assert canBuild(bigWord, bigList) == "pit,sail,space,pride,tile,drug"