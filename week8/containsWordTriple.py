# L is a list of strings
# returns True if there is a triple (s1, s2, s3) such that s1+s2 == s3
# It must run in O(n**2)
# case insensitive
# Example:
# L = ["HELLO","112","cmu", QUIZ","CMU112"] -> returns True ("112", "CMU", "cmu112")
# L = ["ab", "CD", "eF", "cdAB"] -> returns True ("CD", "ab", "cdAB")
def containsWordTriple(L):
    mySet = set()
    for s in L:
        mySet.add(s.lower())
    
    for s1 in mySet:  # n times
        for s2 in mySet:
            s3 = s1 + s2
            if s3 in mySet: # O(1)
                return True
    