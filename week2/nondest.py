"""
Write the function destructiveConvertAllToIntegers(L),
which destructively modifies
the provided list by converting all strings into ints.
Since this
is a destructive function, it should not return any value at all
(so, implicitly, it should return None).
You can assume all strings will represent integers
"""

def nonDestructiveConvertAllToIntegers(L):
    Lcopy = L.copy()
    for i in range(len(Lcopy)):
        if type(Lcopy[i]) != int:
            Lcopy[i] = int(Lcopy[i])
    return Lcopy
    

def testNonDestructiveConvertAllToIntegers():
    print("Testing nonDestructiveRemoveNonIntegers()...", end="")
    l = [3, 7, '5']
    assert(nonDestructiveConvertAllToIntegers(l) == [3, 7, 5])
    assert(l == [3, 7, '5'])
    a = ['1', 2, '3', 4, '15112']
    assert(nonDestructiveConvertAllToIntegers(a) == [1, 2, 3 , 4, 15112])
    assert(a == ['1', 2, '3', 4, '15112'])
    print("Passed.")

testDestructiveConvertAllToIntegers()