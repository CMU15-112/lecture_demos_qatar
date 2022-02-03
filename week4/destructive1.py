"""
Write the function destructiveRemoveNonIntegers(L), which implements the
same function destructively.  Thus, this function should directly modify
the provided list to not have any repeating elements.  Since this
is a destructive function, it should not return any value at all
(so, implicitly, it should return None).
"""

def baddestructiveRemoveNonIntegers(L):
    for e in L:
        if type(e) != int:
            L.remove(e)

# Three versions below, which one do you prefer?

def destructiveRemoveNonIntegersOK1(L):
    for i in range(len(L)):
        if type(L[i]) != int:
            L[i] = 'tag'

    # remove all the tags
    while 'tag' in L:
        L.remove('tag')

def destructiveRemoveNonIntegersOK2(L):
    i =0
    while i < len(L):
        if type(L[i]) != int:
            L.pop(i)
        else:
            i+=1

def destructiveRemoveNonIntegers(L):
    newL = L.copy()
    for e in newL:
        if type(e) != int:
            L.remove(e)


def testDestructiveRemoveNonIntegers():
    print("Testing destructiveRemoveNonIntegers()...", end="")

    l = [3, 2.0, 'cmu']
    assert(destructiveRemoveNonIntegers(l) == None)
    print(l)
    assert(l == [3])
    a = ['1', 2.0, 3, 4, 'hello']
    assert(destructiveRemoveNonIntegers(a) == None)
    assert(a == [3, 4])
    b = ['1', 2.0, 3.0, '4', 'hello']
    assert(destructiveRemoveNonIntegers(b) == None)
    assert(b == [] )
    a = ['1', 2.0, 3, 4]
    assert(destructiveRemoveNonIntegers(a) == None)
    assert(a == [3, 4])


    print("Passed.")


testDestructiveRemoveNonIntegers()
