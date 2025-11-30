import random
L = [-1, 5, 7, -8, 42, -100]
random.shuffle(L)
print("unsorted", L)




# let's sort numbers based on absolute value
# with lamdda we can create functions on the spot
L.sort(key = lambda x: -x if x < 0 else x  )

# these would be equivalent implementations
#L.sort(key = abs)

#def myabs(x):
#    if x < 0:
#        return -x
#    return x
#L.sort(key = myabs )
print(L)
