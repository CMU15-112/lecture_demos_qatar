def longestSubpalidrome(s):
    allsubs = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            allsubs.append(s[i:j+1])
    
    subpal = []
    for sub in allsubs:
        if sub == sub[::-1]:
            subpal.append(sub)
    
    # to be completed
    return  subpal
    
longestSubpalidrome("hello")