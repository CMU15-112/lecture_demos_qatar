#hasDuplicates(L)
#Write the function hasDuplicates(L) that takes a 1d list L of arbitrary values,
#and returns True if L contains any duplicate values
#(that is, if any two values in L are equal to each other), and False otherwise.

def hasDuplicates(L):
    for item in L:
        if L.count(item) > 1:
            return True
    return False
    
    
assert(hasDuplicates([1,2,1]) == True)
assert(hasDuplicates([1,2,3]) == False)
