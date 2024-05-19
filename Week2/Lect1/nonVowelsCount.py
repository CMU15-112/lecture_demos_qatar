def nonVowelsCount(s):
    
    #counter
    counter=0
    
    #iterate over chars in s
    for c in s:
        
        #if c is not vowel
        if c not in "aeiouAEIOU":
            counter+=1
            
    return counter
    
print(nonVowelsCount("Hello"))