def commonKeysDictionary(d1, d2):  # N is size of d1, M is the size of d2 O(N)
    res = {} # empty dict
    for k in d1:  # N
        if k in d2:  # # O(1)
            # k is in d1 and d2
            res[k] = set() # O(1)
            res[k].add(d1[k]) #O(1)
            res[k].add(d2[k]) #O(1)
    return res

# write some tests
dictA = {'hi': 42, 'hello': 67, 'b': 2025}
dictB = {'hi': 56, 'fall': 'break', 'b': 'a'}
assert commonKeysDictionary(dictA, dictB) == {'hi': {42, 56}, 'b': {2025, 'a'}}
print("all tests passed")