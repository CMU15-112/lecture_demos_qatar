def vowelCount(s):
    """
    Takes a string, s, and returns the number of vowels inside s.
    Ignore case, so A and a are both vowels.
    """
    vowels = "aeiouAEIOU"
    cnt = 0
    for c in s:
        if c in vowels:
            cnt += 1
    return cnt

print("Testing vowelCount... ", end="")
assert vowelCount("hello") == 2
assert vowelCount("hello mitochondria") == 7
assert vowelCount("hellO mitochondrIa") == 7
assert vowelCount("uhellO mitochondrIa") == 8
assert vowelCount("") == 0
print("done")

def numberSum(s):
    """
    Return a sum of all of the numbers in a string.
    Example:
    If s is... "I have 21 cats,41dogs, and 30 birds"
    then this will return 92.
    """
    return 42
