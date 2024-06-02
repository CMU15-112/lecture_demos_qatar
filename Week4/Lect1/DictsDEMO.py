### creating dict

# empty
d1= dict()
d2= {}

print(d1)

# from list
L= [(85, 3), (90, 3), (75, 1), (95, 1), (80, 1)]
d3= dict(L)
print("d3", d3)

# statically allocated one
d= {"A": 3, "B": 5, "C":4}
print(d)

d= {"A": 3, "B": 5, "C":4, "B": 3} # overrides the value for a duplicate key
print(d)

# adding/modifying existing element
d["D"]= 10
print(d)

d["D"]= 20
print(d)

# keys follow set properties
l2=[5,6]
#d[l2]= 10 #ERROR (keys can't be mutable)

# values can be anything
d[10]=l2
print(d)

# iterating over dictionaries
print("iterating over keys")
print(type(d.keys()))
for e in d:
   # d[e]= 1
    print(e)
    
for e in d.keys(): 
    print(e)
    
print("iterating over values:")
print(type(d.values()))
for e in d.values():
    print(e)
 
print("iterating over pairs:")
print(type(d.items()))
for e in d.items():
    print(e)

for k, v in d.items():
    print(k)
    print(v)

### Checking Membership
print(d)
print("Membership: ")
print(3 in d) # check keys only
print(3 in d.values())

### Accessing an element
print(d['A']) # returns the val of the given key
#print(d['E']) # error if key doesn't exist

print(d.get('E')) # None if key doesn't exist (No error)
print(d.get('E', 0)) # 0 if key doesn't exist


    



