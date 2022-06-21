# return True or False
def recPalindrome(word):
    if len(word) < 2:
        return True
    else:
        if word[0] != word[-1]:
            return False
        else:
            return recPalindrome(word[1:-1])
            

assert(recPalindrome("racecar") == True)
assert(recPalindrome("hello") == False)
assert(recPalindrome("aabbaa") == True)
assert(recPalindrome("aabcbaa") == True)
assert(recPalindrome("") == True)
assert(recPalindrome("a") == True)
print("Passed!")