# Writing a generator

def evenThenOdd(L): # this would do all the filtering before looping
    return [x for x in L if x % 2 == 0] + [x for x in L if x % 2 == 1]

def evenThenOdd(L): # this is a generator, the filtering happens as we iterate
    # yield evens first
    for x in L:
        if x % 2 == 0:
            yield x

    # then yield odds
    for x in L:
        if x % 2 == 1:
            yield x

obj = evenThenOdd([1, 4, 7, 2, 6, 3]*67676767)
print(obj)
