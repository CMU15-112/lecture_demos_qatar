def letterCounter(s):
    s = s.lower()
    
    res = dict()
    
    for c in s:
        if c.isalpha():
            if c not in res:
                res[c] = 0
            res[c] = res[c] + 1
            
    return res

def areAnagrams(s1,s2):
    return letterCounter(s1) == letterCounter(s2)

#with open("alice.txt","r") as f:
#    aliceText = f.read()
#    letterCounts = letterCounter(aliceText)
#print(letterCounts)