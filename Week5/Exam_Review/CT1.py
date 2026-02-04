def ct1(s):
    t = ''
    for i in range(len(s)):
        t += s[i:] + s[i:][::-1]
    for c in s[::-1]:
        t = (t.replace(c+c,'') + str(t.count(c) + 1))
    print(t)


print(ct1('abcd'))