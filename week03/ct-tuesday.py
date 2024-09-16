def ct1(s, n):
    result = ""
    d = 0
    while n > 0 and len(s) > 0:
        if s[-1].isdigit():
            result += str((n % 100) % int(s[-1]))
        else:
            result += chr(ord("D") + d)
        n //= 10
        s = s[1:-1]
        d += 1
    return result


print(ct1("abc7c3", 2468))
