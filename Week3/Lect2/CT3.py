def f(a, b): 
    b += ["hi"] 
    a = b[:2] 
    return a+b

def ct3(a): 
    b = a 
    c = b[:] 
    b[0] = 42 
    a.append("wow") 
    b = f(a, b) 
    if 42 in c: 
        c.remove(42) 
    print("a1",a) 
    a[-2] = 112 
    print("a2:", a) 
    print("b2:", b) 
    print("c2:", c) 

z = ["feb", 17] 
ct3(z) 
print("z:", z)