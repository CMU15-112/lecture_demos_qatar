### creating dict
print("\n creating dict: ===========")

# empty
d1 = dict()
d2 = {} # empty dict
print(d1)

# from list
L= [(85, 3), (90, 3), (75, 1), (95, 1), (80, 1)]
d3 = dict(L)
print(d3)

# statically allocated one
d = {"A":1, "B": 2, "C":3, "C":4, "D":2}
print(d)


### Adding/Modifying existing element
print("\n Adding/Modifying existing element: ===========")
d["E"] = 5
print(d) # preserves insertion order

d["D"] = 10
print(d)


### Properties: keys follow set properties (unique, immutable)
print("\n Properties: ===========")

L =[1,2]
#d[L] = 5 # crashes.. keys have to be immutable

### Properties: values can be anything
d['F'] = L
print(d)

### iterating over dictionaries
print("\n Iterating : ===========")

for e in d: #keys
    print(d[e])
    print(e)
    
for e in d.keys():
    print(e)
    
print("... over values:")
for e in d.values():
    print(e)
    
print("... over pairs:")
for e in d.items():
    print(e)

for k, v in d.items():
    print(k)
    print(v)
    
### Checking Membership
print("\n Membership: ===========")
print(d)
print(2 in d) #d.keys()
print(2 in d.values())

### Accessing an element
print("\n Accessing an element: ===========")
print(d['A'])
#print(d['S'])

print(d.get('A')) # returns associated value
print(d.get('S')) # None
print(d.get('S', 0))

### Removing an Element
print("\n Removing an Element: ===========")
del d['B']
print(d)

#del d['M']
#d.pop('M')

e  = d.popitem() # last element inserted
print(e)

d.clear()
print(d)

### Adding elements from another iterable (list of tuples or dict)
print("\n Adding Elements from another iterable: ===========")
d.update([('S',3),('M',4)])
print(d)

print(sorted(d.items()))
