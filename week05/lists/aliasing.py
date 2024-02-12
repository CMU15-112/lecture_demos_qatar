a = [1,2,3,4]
b = a

print(f"a: {a}")
print(f"b: {b}")

b[2] = 6

print(f"a: {a}")
print(f"b: {b}")

a += [7,8]

print(f"a: {a}")
print(f"b: {b}")

a = a + [9,10]

print(f"a: {a}")
print(f"b: {b}")

b[0] = 999

print(f"a: {a}")
print(f"b: {b}")

# is...

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)