a = 0.1
print( a == 0.1)

b = 0.1 + 0.1
print( b == 0.2)

c = 0.1 + 0.1 + 0.1
print(c ==0.3)

print(a)
print(b)
print(c)

import math
print(math.isclose(c, 0.3))

def myIsClose(v1, v2):
    return abs(v1-v2) <= 0.000001

print(myIsClose(c, 0.3))
