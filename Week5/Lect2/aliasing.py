import copy


a = [2,3,5,7]
b = a

print(f"a @ {id(a)}")
print(f"b @ {id(b)}")

a[2] = 50
print(b)

# Ctreate a copy

c = []
for e in a:
    c.append(e)

print(f"c @ {id(c)}")
print(c)


e = a[:]
print(f"e @ {id(e)}")
print(e)

f = copy.copy(a)
print(f"f @ {id(f)}")
print(f)


c[1] = 40
print(a)
print(c)

# comparing the objects/content (==) VS comparing references (is)
print("comparing")
print(a == b)
print(a == e)

print(a is b)
print(a is e)

print("after changing e")
e[1] = 100
print(a == e)


# function parameters are aliases
# def f(L):
#     L[0] = 50
#     
#     
# L = [10, 30, 15, 40]
# f(L)
# print(L)


def nonDestructivef(L):
    L2 = sorted(L)
    return L2
    
    
L = [10, 30, 15, 40]
nonDestructivef(L)
print(L)

