import copy

a = [
      [1,2],
      [3,4]
    ]


b = a #alias

print("Copy: ")
c = copy.copy(a)
c[1][0] = 10
print("a:", a)
print("b:",b)
print("c:",c)

print("Deep Copy:")
d = copy.deepcopy(a)
d[1][0] = 20
print("a:", a)
print("d:",d)

