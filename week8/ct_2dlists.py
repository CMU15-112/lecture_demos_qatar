import copy

def ct1(M):
    a = M
    b = copy.copy(L)
    c = copy.deepcopy(L)
    b[1][1] = c[0][0]
    c[1].append(b[1][0])
    a[0] = b[1]
    a[0][0] += b.pop()[0]
    return a,b,c

L = [[1],[2,5]]
ret = ct1(L)
for val in ret:
    print(val)
print(L)
