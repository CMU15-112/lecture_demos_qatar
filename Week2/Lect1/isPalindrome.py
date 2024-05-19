'''
Write the Function nonVowelsCount(s) that takes a string s
and returns number of non-vowels inside s.
Ignore case, A and a are both vowels.
'''
def isPalindrome(s):
    
    filteredS= "" 
    for c in s: # take one char at a time
        if c.isalnum(): # if this c is alpha-numeric
            filteredS+=c.lower() # add this c to the filteredS
            
    # fileterdS all char that are alpha-numeric in lower case
    return filteredS == filteredS[::-1] # it reads the same fwd and bwd

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("Hello"))