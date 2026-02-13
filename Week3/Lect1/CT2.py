def ct2(s):
    result = ""
    i = 0
    for c in s:
        if c.isdigit():
            result += s[int(c)]
        elif c == c.upper():
            i += 3
        else:
            result += s[i % 2]
        i += 1
    return result

s = "x3Y5cA"
print(ct2(s))