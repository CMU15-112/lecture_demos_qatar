"""Write the function largestNumber(s) that takes a string s
and returns the largest int value that occurs within that text, or None if no such value occurs.
You may assume that the only numbers in the text are non-negative integers
and that numbers are always composed of consecutive digits (without commas, for example).

    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")==17)
    assert(largestNumber("I saw four dogs")==None)

"""

"""
One example
s = I saw 3 dogs, 17 cats, and 14 cows

split into words, I get a list

[I, saw, 3, dogs, 17, cats, ..]

loop through each word and check if all letters are digits

[3, 
I. no
saw. no
3 yes

[3,17,14]
we have this list
take max

17
"""

def largestNumber(s):
    tokens = s.split()
    maxnum=None
    for token in tokens:
        if token.isdigit():
            number = int(token)
            if maxnum==None:
                maxnum=number
            maxnum=max(maxnum, number)
    return maxnum

    
    
def testLargestNumber():
    print("Testing largestNumber...",end="")
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!")==17)
    assert(largestNumber("I saw four dogs")==None)
    # Try to write another solution that takes into account this type of testcases:
    #assert(largestNumber("This is difficult15112case")==15112)
    print("passed")

testLargestNumber()