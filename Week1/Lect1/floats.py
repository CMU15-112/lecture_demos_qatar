a = 0.1
print(a == 0.1)

b = 0.1 + 0.1
print(b == 0.2)

c = 0.1 + 0.1 + 0.1
print(c == 0.3)
print(c)


import math

print(math.isclose(c, 0.3))
print(abs(c-0.3) < 0.00001)

