# Efficiency as the number of steps a program takes to run with respect to
# its input.

L = [8, 83, 4, 9, 4, 4, 8]

i = 0 # 1 step
for item in L: # Runs N times, where N is the length of L
    i += item # 1 step
# Total number of steps: 1 + N steps
# ... or O(N)

biggest = -1 # 1 step
for item in L: # Runs N times
    if item > biggest: # 1 step
        biggest = item # 1 step
# Total number of steps: 1 + 2*N
# ... or O(N)

i = 0 # 1 step
biggest = -1 # 1 step
for item in L: # Runs N times
    i += item # 1 step
    if item > biggest: # 1 step
        biggest = item # 1 step
# Total number of steps: 2 + 3*N
# ... or O(N) [linear]
# If N is 100, steps = 302
# If N is 1000, steps = 3002

mostFrequent = 0 # 1 step
mostFrequentCnt = 0 # 1 step
for item in L: # Runs N times
    cnt = L.count(item) # About N steps
    if cnt > mostFrequentCnt: # 1 step
        mostFrequentCnt = cnt # 1 step
        mostFrequent = item   # 1 step
# Total number of steps: 2 + N * (N + 3) = N**2 + 3N + 2
# ... or O(N**2)
# If N is 100, steps =    10302
# If N is 1000, steps = 1000302

L.sort() # This is O(N * log N)

# Common mistakes

# This is O(N), not O(N**2) because the loops aren't nested
def f(L):
    i = 0 # O(1)
    for item in L: # Runs N times
        i += item # O(1)

    biggest = -1 # O(1)
    for item in L: # Runs N times
        if item > biggest: # O(1)
            biggest = item # O(1)
    
    return (i,biggest) # O(1)

# O(N)
def g(s):
    theNumbers = "0123456789"
    cnt = 0
    for char in s: # Runs N times
        if char in theNumbers: # O(1)
            cnt += 1 # O(1)
    return cnt # O(1)
        
# O(N**2)
def h(s):
    for i in range(len(s)): # Runs N times
        if s[i] in s[i+1:]: # O(N)
            return True # O(1)
    return False # O(1)

# O(N)
def j(s):
    theNumbers = "0123456789"
    cnt = 0
    for char in s: # Runs N times
        for c2 in theNumbers: # Runs 10 times, ie O(1)
            if char == c2:
                cnt += 1
    return cnt

# O(N)
def k(s):
    cnt = 0
    for char in s:
        if char.isdigit():
            cnt += 1
    return cnt

def combo(s):
    a = k(s) # O(N)
    b = j(s) # O(N)
    c = h(s) # O(N**2)
# O(N**2)