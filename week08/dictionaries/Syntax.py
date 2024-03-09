'''
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
'''

#### creating

d= dict()
print(d)
d={}
print(d)

L= [(85, 3), (90, 3), (75, 1), (95, 1), (80, 1)]
d= dict(L)
print(d)

ages={'Ali': 20, "Sara": 25}
print(ages)


#### properties

#keys- unordered, unique, immutable
ages["Sara"]= 20 # if the key exists, it will just update its value
print(ages)

ages["Nora"]= 30 # if the key doesn't exist, it will add the value
print(ages)

#ages[[2,1]]= 20 #immutable

# values can be anything
ages["kids"]= [5, 10, 13]
print(ages)

ages["kids"][1]=15 
print(ages) # what should this print?



#### Retrieving Elements

# retrieve a value for [key]
print(ages["kids"])
#print(ages["Amna"]) # Error


print(ages.get("kids"))
print(ages.get("Amna")) #None
print(ages.get("Amna", "Not Found"))


# remove last inserted element
(k,v)= ages.popitem() 
print(k,v)

#can get all keys in dict
print(ages.keys())

# can get all values
print(ages.values())


#### Iterating Over elements OR checking membership (in)

#by default - keys

for e in ages: # ages.keys()
    print(e)

for e in ages.values():
    print(e)

for  (k,v) in ages.items():
    print(k,v)

# same thing for membership
print("Nora" in ages)
print(30 in ages) # what should this return?
print(30 in ages.values())


#### Adding elements from another iterable
ages.update({"Sara":35, "Haya": 30})
print(ages)
print(len(ages))

##### removing elements
# one element
del ages["Sara"]

# clearing all elements
ages.clear()


