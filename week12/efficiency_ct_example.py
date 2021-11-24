def f1(L):
    d = {}
    for item in L:
        d[type(item)] = d.get(type(item),0)+1
    
    a = None
    for k in d:
        if a == None or d[k] > d[a]:
            a = k
    return (a,d[a])

def f2(L):
    r = (None, 0)
    for item in L:
        t = 0
        for x in L:
            if type(x) == type(item):
                t += 1
        if t > r[1]:
            r = (type(item),t)
    return r
    
L = ["112", 5, "Peanuts", False, 1, "hi", 3.0, None, True]
print(f1(L))
print(f2(L))