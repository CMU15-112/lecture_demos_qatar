import copy

a = [
      [1,2],
      [3,4]
    ]

b = a
c = copy.copy(a)
d = copy.deepcopy(a)

c[1][0] = 10

print(a)
c.append([50,60])
c[0] = [7,8]
c[0][1] = 15