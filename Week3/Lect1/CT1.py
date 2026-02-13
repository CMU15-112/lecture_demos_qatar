def f1(s):
    return s[::2][::-1] + s[::-1][::2]

def f2(s):
    s = s[: len(s) // 2] + s[len(s) // 4 : len(s) - 1]
    return s

def ct1(magic):    
    print("1: ", f1(magic))
    print("2: ", f2(magic))
    return magic

print(ct1("112rocks"))