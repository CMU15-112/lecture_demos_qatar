import copy

def ct(a):
    (b,c,d) = (a, copy.copy(a), copy.deepcopy(a))
    print ((a == b), (a == c), (a == d))
    print ((a is b), (a is c), (a is d))
    print ((a[0] is b[0]), (a[0] is c[0]), (a[0] is d[0]))     
    a[0] += [5]
    b[1] = [5, 6]
    c[1][0] += 10
    d[0] = c[1]
    for L in [a,b,c,d]:
        print(L)

a = [[1], [2,3,4]]
ct(a)
print(a)