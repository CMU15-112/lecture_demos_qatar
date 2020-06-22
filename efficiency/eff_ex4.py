def f2(L): # L contains N items                 # Big-O
    allowedWords = ["cat", "dog", "rat"]        # O(1)
    newList = []                                # O(1)
    for w in L:                                 # O(N)
        if w in allowedWords:                   # O(1)  
            newList.append(w)                   # O(1)
    for w in allowedWords:                      # O(1)
        if w in L:                              # O(N)
            L.remove(w)                         # O(N)
        L.sort()                                #_O(NlogN)_
    L.extend(newList)                           # O(N)
    return L                                    # O(1)


# for lists
#item in L  O( len(L) ) -> O(N)
#w in allowedWords  -> O(len(allowedWord)) -> O(3) -> O(1)