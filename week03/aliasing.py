import copy

a = [1, 2, 3, 4]
b = a

c = a[:]
# c = copy.copy(a)

b[0] = 10

print(a)
print(b)
print(c)