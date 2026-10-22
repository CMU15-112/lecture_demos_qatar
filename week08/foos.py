def foo(lst):
    v = 43 # 1 op
    if len(lst) > 0: # 2 ops
        return L[0] * 3 # 2 ops
    return 42 # 1 op
    # Best: 4 steps
    # Worst: 5 steps
    # O(1)

# Assume that lst contains N items
def foo(lst):
    i = 0 # 1 op
    result = [] # 1 op
    # This loop runs N-1 times
    while i < len(L): # 2 op
        result += L[i] # 2 op
        i += 1 # 1 op
    return i # 1 op
    # 1 + 1 + (N)(2 + 2 + 1) + 1 = 1 + 
    