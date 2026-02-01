#Write a function that takes a list and returns a list with all duplicates

def findDups(L):
    
    dupL = []
    
    for e in L:        
        if L.count(e) > 1 and e not in dupL:
            dupL+=[e]
            
    return dupL

print(findDups([1,2,3,4,1,6,1,2,5,3]))



