def ct(a, b, d=0):
    print(f"a:{a} b:{b} d:{d}")
    n = b - a
    if n <= 1:
        return
    ct(a, a+n//2, d+1)
    ct(a+n//2, b, d+1)
ct(0,3)