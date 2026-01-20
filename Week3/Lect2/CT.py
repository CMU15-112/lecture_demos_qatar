def ct(s):
    r = ""
    while (len(s) > 1):
        r += s[:1] + s[2:4] + "-"
        s = s[1:len(s)-1]
        if s.isalpha():
            s = s.upper()
        print(s)
    return r + s

print(ct("abcd123"))