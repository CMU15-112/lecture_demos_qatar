def nondestructiveRemoveNonInts(L):
    Lints = []
    for e in L:
        if isinstance(e, int):
            Lints.append(e)
    return Lints


L = [112, '15', 4, 2, 'hey', 15.112]
assert(nondestructiveRemoveNonInts(L) == [112, 4, 2])
assert(L == [112, '15', 4, 2, 'hey',  15.112])