"""
Write the function largestNumber(text) that takes a string of text
and returns the largest int value that occurs within that text,
or None if no such value occurs.
You may assume that the only numbers in the text
are non-negative integers and that numbers are always
composed of consecutive digits (without commas, for example).
For example:
"""

def testLargestNumber():
    print("Testing largestNumber...",end="")
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")==17)
    assert(largestNumber("I saw four dogs")==None)
    assert(largestNumber("This is difficult15112case")==15112)
    print("passed")

testLargestNumber()