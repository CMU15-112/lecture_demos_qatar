def rc2(L):
    assert(isinstance(L, list) and (len(L) == 5))
    for i in range(-2, 2):
        assert(L[i] == L[i+1] + i)
    return (sum(L) == 20)