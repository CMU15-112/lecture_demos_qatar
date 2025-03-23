def myMysteryFunction(s):
    value = 0
    for c in s:
        if c in "aeiou":
            value += 1
    return value


print(myMysteryFunction("hello"))