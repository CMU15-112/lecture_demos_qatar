s = "Hi there, my name is Bob"
for token in s.split(","):
    print(token)
    
s = "Hi there"
for c in s:
    print(c,end="")
    if c == "t":
        s = s.replace("i", "")
        s = s.replace("H", "")
print()

s = "Hi there"
for i in range(len(s)):
    c = s[i]
    print(c,end="")
    if c == "t":
        s = s.replace("i", "")
        s = s.replace("H", "")
print()