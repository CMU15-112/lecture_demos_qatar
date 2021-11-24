L = [52, 83, 78, 9, 12, 4, 8]

i = 0 # 1 step
for item in L: # Runs N times
    i += item # 1 step
    
# Total number of steps: 1 + N steps
# O(N)

















################################

L = [52, 83, 78, 9, 12, 4, 8]
# Assume that L has N items
i = 0  # 1 step
biggest = -1  # 1 step
for item in L: # Repeat N times
    i += item # 1 step
    
    if i > biggest: # 1 step
        biggest = i # 1 step
        
# Total steps: 2 + 3*N steps
# O(N)














################################

L = [1, 2, 3, 1, 4, 2, 1, 5, 6, 1]

mostFrequent = 0 # 1 step
mostFrequentCnt = 0 # 1 step
for item in L: # Repeat N times
    cnt = L.count(item) # 2N + 2 steps
    if cnt > mostFrequentCnt: # 1 step
        mostFrequentCnt = cnt # 1 step
        mostFrequent = item # 1 step
        
# Steps: 2 + N * (2*N+5) == 2N^2 + 5N + 2
# O(N^2)



###################################
mostFrequent = 0
mostFrequentCnt = 0
for item in L: # Runs N times
    cnt = L.count(item) # N
    if cnt > mostFrequentCnt: 
        mostFrequentCnt = cnt 
        mostFrequent = item
# O(N^2)









################################

# Some built-ins...
if 4 in L: # O(N)
    print("hi")

# What about operating on sets?
s = set(L) # O(N)
if 4 in s: # O(1)
    print("hi")

# What about sorting?
L.sort() # O(N log N)

################################

def f(L): # O (N log N)
    L1 = sorted(L)
    return L1

def g(L): # O(N^2)
    L1 = L * len(L)
    return L1

L = [52, 83, 78, 9, 12, 4, 8]
L = g(f(L)) # N log N + N^2 -> O(N^2)
M = f(g(L)) # N^2 + N^2 log N^2 -> O(N^2 log N)
