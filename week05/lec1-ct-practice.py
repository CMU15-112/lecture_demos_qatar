import copy

def ct(a):
    b = a
    c = copy.copy(a)
    b[0] = 64
    a.append("wow")
    c[3] = 2 * c[3]
    #b = b[:2] + ["hi"] + b[2:]
    b = b[::]
    b[1] = "bob"
    c.pop(1)
    a[-2] = 112
    print("a:", a)
    print("b:", b)
    print("c:", c)

z = ["feb", 14, "2020", 180]
ct(z)
print("z:", z)