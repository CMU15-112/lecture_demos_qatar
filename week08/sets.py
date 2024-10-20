s = set()
print(s)

L = [5, 10, 15, 20]
s = set(L)
print(s)

s = {5, 10, 15, 20, "A", "B"}
print(s)

L1 = [1, 2, 3, 4]
s1 = set(L1)
L2 = [4, 3, 2, 1]
s2 = set(L2)
print(L1 == L2)
print(s1 == s2)

print(L1[0])
#print(s1[0])

# Can only contain immutable items
s = {1, "Hello", 2.5, (3, 4)}
print(s)
#s = {1, 2, [3,4]}

print("----")
for e in s:
    print(e)
    

s.add("Hey there")
print(s)
s.update({5, 6, 1})
print(s)

s.remove(1)
print(s)

#s.remove("red")
s.discard("red")
print(s)

s = {1, 2}
t = s.union({1, 4, 5})
# t = s | {1,4,5}
print(s, t)
t = s.difference({1,3})
#t = s - {1,3}
print(s, t)

