import copy
"""

a = [ [1,2],[4,5] ]
b = copy.copy(a)
c = copy.deepcopy(a)

b[0][0] = 10

b[0] = [11,12]

print(a)
print(b)
print(c)
"""

a = [[0]*2]*3
b = copy.deepcopy(a)
b[0][0] = 6
a[0][1] = 7

print(a)
print(b)