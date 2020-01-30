import copy

a = [1,2,3,4]
b = a
c = copy.copy(a)
b[0] = 6
c[0] = 5

print(a)
print(b)
print(c)

