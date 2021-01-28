import math

def absoluteValue(n):
    if n < 0:
        return -n
    else:
        return n
    
a = 0.1 + 0.1 + 0.1
print(a)
print(a == 0.3) # Bad idea

if absoluteValue(0.3-a) < 0.00000001:
    print("It is 0.3!")
else:
    print("It isn't 0.3")
    
if abs(0.3-a) < 0.00000001:
    print("It is 0.3!")
else:
    print("It isn't 0.3")
    
if math.isclose(a, 0.3):
    print("It is 0.3!")
else:
    print("It isn't 0.3")    