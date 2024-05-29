import copy

def ct1(a):
    a = sorted(a)
    b = a
    c = copy.copy(a)
    d = b[:]
    a[0] += 5
    b[1] = 6
    c[2] = 7
    d[3] -= 11
    b.append("Cat")
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"c: {c}")
    print(f"d: {d}")

a = [50, 30, 40, 20]
print(ct1(a))
print(a)