def roc(L):
    return mystery(L, 2, 0)

def mystery(L, v, d):
    assert (v == L[0])
    if len(L) == 1:
        return d == 4
    return mystery(L[1:], v+L[0], d+1)

print(roc([2,4,8,16,32]))
