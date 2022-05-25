"""
Write the function destructiveConvertAllToIntegers(L),
which destructively modifies
the provided list by converting all strings into ints.
Since this
is a destructive function, it should not return any value at all
(so, implicitly, it should return None).
You can assume all strings will represent integers
"""

def destructiveConvertAllToIntegers(L):
    for i in range(len(L)):
        if type(L[i]) != int:
            L[i] = int(L[i])
    

def testDestructiveConvertAllToIntegers():
    print("Testing destructiveRemoveNonIntegers()...", end="")
    l = [3, 7, '5']
    assert(destructiveConvertAllToIntegers(l) == None)
    assert(l == [3, 7, 5])
    a = ['1', 2, '3', 4, '15112']
    assert(destructiveConvertAllToIntegers(a) == None)
    assert(a == [1, 2, 3 , 4, 15112])
    print("Passed.")

testDestructiveConvertAllToIntegers()