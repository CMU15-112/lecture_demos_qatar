def ct1(m):
    x = 1
    while x < 6:
        if x%5 == 0:
            break
        x += 2
        print("x =", x)
    for y in range(m, m+3):
        if y % 3 == 0:
            print("mul3 = ", y)
        elif y % 2 == 0:
            print("even")
        else:
            x += y
    return x

print(ct1(4))