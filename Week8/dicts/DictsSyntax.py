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
print(d)

d["D"] = 10
print(d)

### Properties: keys follow set properties (unique, immutable)
print("\n Properties: ===========")

L =[1,2]
#d[L] = 5 # crashes.. keys have to be immutable

### Properties: values can be anything


### iterating over dictionaries
print("\n Iterating : ===========")

print("... over keys")

    
print("... over values:")

print("... over pairs:")


### Checking Membership
print("\n Membership: ===========")


### Accessing an element
print("\n Accessing an element: ===========")


### Removing an Element
print("\n Removing an Element: ===========")




