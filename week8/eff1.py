def myFunction1(L):
    result = L[0] + L[1] # (1)
    return result

# 1 instruction


# 4 instructions
def myFunction2(L):
    if L[0]%2 == 0:
        L[0] = 1
        L[1] = 2
        L[2] = 3

# 2n + 1 instructions
def myFunction3(L):  # n = len(L)
    tot=0 # 1
    for i in L:  # n times         
        if i%2 == 0:  # 2
            tot += i
        else:
            tot -= i
    return tot

# 1 + 2n + 2n = 1 + 4n
def myFunction4(L):
    tot=0  # 1
    for i in L:   #n times
        if i%2 == 0:  #2
            tot += i
    for i in L:  # n times
        if i%2 == 1:  #2
            tot -= i
    return tot


# instructions:
# 1 + 2n + 2n + 2 = 4n + 3 = O(n)

def myFunction5(L):
    tot=0
    for i in L:  # O(n)
        if i%2 == 0:
            tot += i
    for i in L:
        if i%2 == 1:
            tot -= i
    if tot > 100:  #O(1)
        tot = tot ** 2
        return tot
    else:
        return tot

# 1 + n*(n+1) = 1 + n^2 + n
def myFunction(L):  # n = len(L)
    maxfreq=0
    for i in L: # n times
        c = L.count(i)   # n
        maxfreq = max(maxfreq, c) # 1
    return maxfreq

# O(1)
# n, 4n, 4n+3, 1000n, 7n+1000 -> O(n)
# n**2, 4n**2, 4n**2+3, 1000n**2 + 10n, 7n**2+1000n -> O(n**2)

# What if we have two functiosn f and g that execute 7*n**2+1000*n and n**2 respectively
# Both have the same complexity
# O(n**2) and O(n**2)
# If n = 10, f executes 10700 instructions and g executes 100, big difference
# But when n is large, n=100000, then the difference is not that significant




