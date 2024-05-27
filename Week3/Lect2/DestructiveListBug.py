#There's a bug in the following code!

def destructiveRemoveNonIntsWrong(L):
    for e in L: # L[:]:
        print("Checking", e)
        if not isinstance(e, int):
            L.remove(e)    

L = [112, '15', 4, 2, 'hey',  15.112]
assert(destructiveRemoveNonIntsWrong(L) == None)
print(L) # it never checks 4 or 15.112. why? 
assert(L == [112, 4, 2])

