d = dict()
print(d)

ages = {'Ali':25, 'Sara':20}

ages["Sara"] = 30
print(ages)

ages["Nora"] = 35
print(ages)

print(ages["Sara"])
print(ages.get("Sara"))

#print(ages["Ahmed"])
print(ages)
print(ages.get("Ahmed"))

ages["Ahmed"] = None
print(ages)
print(ages.get("Ahmed"))

print(ages.get("Bob", 0))

print("Nora" in ages)
print("Bob" in ages)

### Keys and Values
print(ages.keys())
print(ages.values())

for k in ages:
    print(k, ages[k])
    
for v in ages.values():
    print(v)
    
for k,v in ages.items():
    print(k, v)










### Crazy ###
import copy
d = dict()
L = [1, 2, 3, 4]
d["bob"] = L
d[6] = L
t = copy.deepcopy(d)
#print(d)
d[6][0] = 78
t[6][0] = 79
#print(d)
#print(t)
