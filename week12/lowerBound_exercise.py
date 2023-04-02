def lowerBound(L, x):
    pass

L = [4,7,9,11,12,13,15,16,17]

assert(lowerBound([4,7,9,11,12,13,15,16,17], 4) == None)
assert(lowerBound([4,7,9,11,12,13,15,16,17], 5) == 4)
assert(lowerBound([4,7,9,11,12,13,15,16,17], 6) == 4)
assert(lowerBound([4,7,9,11,12,13,15,16,17], 7) == 4)
assert(lowerBound([4,7,9,11,12,13,15,16,17], 8) == 7)
assert(lowerBound([4,7,9,11,12,13,15,16,17], 20) == 17)