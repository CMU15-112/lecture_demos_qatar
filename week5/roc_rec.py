"""
Find the value of L s.t. roc(L) returns True

Hints:
- What's the type of L? list? string?


"""

def roc(L):
    return mystery(L, 64, 0)

def mystery(L, v, d):
    print(L, v, d)
    assert (v == L[-1])
    if len(L) == 1:
        return d == 4
    return mystery(L[:-1], L[-1] - L[-2], d+1)