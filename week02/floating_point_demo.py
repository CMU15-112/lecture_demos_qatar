import math

a = 0.1 + 0.1 + 0.1
print(a)
print(a == 0.3) # Bad idea
print(math.isclose(a, 0.3)) # Good idea
