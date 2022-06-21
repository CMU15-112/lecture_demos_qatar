# how many instructions?
# 5
def myFunction(L):
    result = L[0] + L[1]  #L[0], L[1], add, assign
    return result  # return result

# 6
# n = len(L)
def myFunction(L):
    if L[0]%2 == 0:  # L[0], doing mod, compare with 0
        L[0] = 1
        L[1] = 2
        L[2] = 3
        
        
        
# assume len(L) = n
# 1 + 4n + 4 = 4n + 5= O(n)

def myFunction(L):
    tot=0  # 1 instruction
    for i in L:   # loop n times: 4 inst = 4n
        if i%2 == 0:  
            tot += i
        else:
            tot -= i
    tot = tot * 4  # 2
    if tot > 8:  # 1
        return False #1
    return tot





# 1 + n*(n+1) + 1 = 1 + n^2 + n + 1
# O(n^2)
def myFunction(L):  # n = len(L)
    maxfreq=0  # 1
    for i in L: # n iter. 
        c = L.count(i) # n instruc 
        maxfreq = max(maxfreq, c) #1 
    return maxfreq #
















# n = len(L)

# 1000 + 2
# O(1)
def myFunction(L):
    for i in range(1000):  #1000 it
        if i < len(L):     # 1 
            print(i)       # 1


# 1, 3,  6, 10, 2000 -> 1  -> O(1)  O(1000)
# n, 2n+3 , 4n+1, 0.0001n -> n  O(n)
# n^2, 3n^2, 1 + 2n^2 + n -> O(n^2)  (take always the biggest term)




