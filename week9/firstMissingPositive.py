def firstMissingPositive(L):
    s = set(L)
    for i in range(1, len(L)+1):
        if i not in s:
            return i
    return len(L)
