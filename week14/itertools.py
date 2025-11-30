# itertools provides helpful iterators and generators
from itertools import permutations

# checking the validity of a permutation of (,)
def isValid(expr):
    n = 0
    for e in expr:
        if e == '(':
            n += 1
        else:
            n -= 1
        if n < 0:
            return False
    return n == 0


def generateParentheses(n):
    res = set()
    for per in permutations('()'*n, 2*n):
        expr = "".join(per)
        if isValid(expr):
            res.add(expr)

    return res

print(generateParentheses(4))
