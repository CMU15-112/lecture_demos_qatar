"""
Write the function nondestructiveRemoveNonIntegers(L), which
#takes a list L and nondestructively returns a new list in
which any non integer items in L are removed.
"""

def nondestructiveRemoveNonIntegers(L):
    newL = []
    for e in L:
        if type(e) == int:
            newL.append(e)
    return newL


def testNonDestructiveRemoveNonIntegers():
    print("testing nondestructiveRemoveNonIntegers...", end="")
    assert( nondestructiveRemoveNonIntegers(['1', 2.0, 3, 4, 'hello']) == [3,4])
    assert( nondestructiveRemoveNonIntegers(['1', 2.0, 3.0, '4', 'hello']) == [])
    print("passed")

testNonDestructiveRemoveNonIntegers()
