d = dict()
d[100] = 5
d[200] = 8
d[300] = 7
d[100] = 9
print(d)

# Iterate over items in a dictionary
print("---")
for e in d:
    print(f"key {e} has value {d[e]}")
    
del d[100]

#print(d[100])

print(d.get(100, -1))

for (key, value) in d.items():
    print(f"key {key} has value {value}")
   



