a = [15]

a.append(1)
a += [2]
print(a)

print("---")
c = a + [3]
print(a)
print(c)

print("---")
print(a)
a + [10,50,100]
print(a)

print("---")
b = sorted(a)
print(a)
print(b)

a.sort()
print(a)

c = [432,423,423,64,76,5685,423,654,78,6,5,8,7,695,368,6]
sorted(c) # This, alone, does not sort c.
print(c)
c.sort()
print(c)

c.reverse()
print(c)