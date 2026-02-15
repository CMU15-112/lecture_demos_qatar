import copy

def ctAlias(L):
    a = L
    b = copy.copy(L)
    c = copy.deepcopy(L)
    a[0][0] = 10
    b[1][1] = "cat"
    c[0][1] = 3.4
    a.append("Bob")
    b.append("Ahmed")
    c.append("Noor")
    print(a)
    print(b)
    print(c)

L = [[0,1,2],[3,4,5]]
ctAlias(L)
print(L)