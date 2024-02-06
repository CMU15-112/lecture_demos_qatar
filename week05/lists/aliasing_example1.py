def f(L):
    L[0] = 15
    L.append(1)
    
def ct(L):
    L = L + [1]
    M = L
    f(L)
    L += [1]
    if M is L:
        M[3] = 2
    print(L, M)
    
L = [0]
ct(L)
print(L)