def letterCount(s, c):
    s = s.lower()
    c = c.lower()
    cnt = 0
    for letter in s:
        if letter == c:
            cnt += 1
    return cnt

# Return the number of vowels in s
def vowelCount(s): 
    s = s.lower()
    
    cnt = 0
    for letter in s:
        if letter == 'a' or letter == 'e' or letter == 'i' \
           or letter == 'o' or letter == 'u':
            cnt += 1
    return cnt
    
# Return the number of vowels in s
def vowelCount(s):     
    cnt = 0
    for letter in s:
        if letter in "aeiouAEIOU":
            cnt += 1
    return cnt
    
def interleave(s1, s2):
    res = ""
    
    minLen = min(len(s1), len(s2))
    
    for i in range(minLen):
        res += s1[i]
        res += s2[i]
    
    # Copy the rest of the larger string
    if len(s1) > len(s2):
        res += s1[minLen:]
    else:
        res += s2[minLen:]
    
    return res
            
    
assert(interleave('pto', 'yhn') == "python")