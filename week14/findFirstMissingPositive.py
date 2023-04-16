def firstMissingPositive(L):
    s = set(L)
    for i in range(1,43):
        if i not in s:
            return i
    return None