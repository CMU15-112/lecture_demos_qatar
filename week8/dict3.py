# # No duplicate keys allowed
print("---")
d = dict()
d[100] = 5
d[200] = 8
d[300] = 7
d[100] = 9

print(d)

print("---")
for key in d:
    print(f"key {key} has value {d[key]}")

for (key, value) in d.items():
    print(f"key {key} has value {d[key]}")

print("dict len is ", len(d))

#d.pop(100)
del d[100]

print(d)
