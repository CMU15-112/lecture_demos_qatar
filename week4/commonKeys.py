"""
Write the function commonKeysDictionary(d1, d2) that takes two dictionaries
and combines them into a single new dictionary. (non-destructive)
The combined dictionary should contain only keys that are present in both dictionaries.
The value of each key in the combined dictionary should be the
set of values associated with that key from
the given dictionaries.
For example given d1 = {"a": 1, "b": 2} and d2 = {"a": 3, "c": 4}
commonKeysDictionary(d1, d2) returns {"a": {1, 3}},
because the only key that is present in both
dictionaries is a. :
"""
assert(commonKeysDictionary({"a": 1, "b": 2, "c":42}, {"a": 1, "c": 4} ) 
       == {"a": {1}, "c": {4, 42}})
assert( commonKeysDictionary({"a": 1, "b": 2},{"a": 3, "c": 4}) == {"a": {1,3}})
assert( commonKeysDictionary({"a": 1, "b": 2},{"c": 3, "d": 4}) == dict())

def commonKeysDictionary(d1, d2):
    res = {}
    for k in d1:
        if k in d2:
            res[k] = {d1[k], d2[k]}
    return res

    
