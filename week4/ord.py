# chr
print(ord('a'))
print(ord('b'))
print(ord('1'))

"""
Write the function getPosition(c) that
takes one lowercase alphabetic character c and
return its 0-based position in the English alphabet
"""

"""
b
ord('b') = 98
ord(b) - ord(a) = 98 - 97 = 1
121 - 97 = 24
"""

def getPosition(c):
    return ord(c) - ord('a')
    

def testGetPosition():
    assert( getPosition('a')==0)
    assert( getPosition('b')==1)
    assert( getPosition('z')==25)
    print("passed")
    
testGetPosition()