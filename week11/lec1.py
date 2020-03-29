# Efficiency as described by the # of steps
L = [52, 83, 78, 9, 12, 4, 8]
#L = [1,   2, 3,  4, 5,  6, 7]

i = 0 # 1 step
for item in L: # Runs N times
    i += item # 1 step (inside the loop)
# total steps: 1 + N
# Big-O:  O(N)

# Assume that L has N items
i = 0 # 1 step
biggest = -1 # 1 step
for item in L: # Runs N times
    i += item # 1 step (inside the loop)
    
    if i > biggest: # 1 step (inside the loop)
        biggest = i # 1 step (inside the loop)
# total steps: 2 + N*3
# Big-O:  O(N)

# Analysis of Linear:
# Assuming that...
# N = 20, it takes 200 steps.
# then...
# if N = 40, it takes 400 steps.

L = [1, 2, 3, 1, 4, 2, 1, 5, 6, 1]

mostFrequent = 0  # 1 step
mostFrequentCnt = 0  # 1 step
for item in L: # Runs N times
    cnt = L.count(item)  # N steps
    if cnt > mostFrequentCnt: # 1 step
        mostFrequentCnt = cnt # 1 step
        mostFrequent = item # 1 step
# total steps: 2 + N*(N + 3) = N^2 + 3*N + 2
# Big-O: O(N^2)

# Analysis of Quadratic:
# Assuming that...
# N = 20, it takes 200 steps.
# then...
# if N = 40, it takes 800 steps

# To know:
L.sort() # O(N log N)

# Another example:

def f(L):
    L1 = sorted(L) # O(N log N)
    return L1      # O(1)

def g(L):
    L1 = L * len(L) # O(N^2)
    return L1        # O(1)

L = [52, 83, 78, 9, 12, 4, 8]
L = g(f(L)) # O(N log N) + O(N^2) => O(N^2)
M = f(g(L)) # O(N^2) + O(N^2 log N^2) => O(N^2 log N)
