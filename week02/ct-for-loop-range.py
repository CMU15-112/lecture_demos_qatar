def f(n, m):
    total = 0
    for x in range(n, m - 1, -1):
        if x % 2 == 1:
            total += x
    return total

print(f(15, 10))