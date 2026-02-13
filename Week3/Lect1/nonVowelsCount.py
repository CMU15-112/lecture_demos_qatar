'''
Write the Function nonVowelsCount(s) that takes a string s
and returns number of non-vowels inside s.
Ignore case, A and a are both vowels.
'''
def nonVowelsCount(s):
    
    c = 0
    vs = "aeiouAEIOU"
    
    for x in s:
        if x not in vs:
            c+=1
            
    return c
    
print(nonVowelsCount("Hello"))