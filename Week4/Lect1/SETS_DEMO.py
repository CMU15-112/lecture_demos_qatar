### Creating a set

# from list
L= ['hello', 'world', 'hello']
s1= set(L) # ignores duplicates
print(s1) 

# from string
s= "Hello"
s2= set(s) # ignores duplicates
print(s2)

# empty set
es= set()
print(es)

es2= {} # an empty dict
print(type(es2))

# statically allocated set
s3= {1, 2, 3, 3, "A", "B"}
print(s3)

### set elements are unordered
L1 = [1,2,3,4]
L2= [1,3,2,4]
print(L1==L2) # False (lists are ordered)

s4= set(L1)
s5= set(L2)
print(s4==s5) # True


#print(s3[0]) # can't index sets

### set elements are immutable
s3= {1, 2, 3, 3, "A", "B"} #, [1,2]} # a list can't be a set element
print(s3)
print(hash("Hello"))

### Iterarting over elements & Membership
for e in s3:
    print(e)
    
print(1 in s3)
print(2 not in s3)

### Adding Elements
s3.add("C") # single element
print(s3)

s3.update([3,5,6]) # multiple elements from iterable data type (e.g. list, string, tuple, set)
print(s3)


### Removing elements
s3.remove(1)
print(s3)

#s3.remove(1) # throws error if element doesn't exist
#print(s3)


print("discard")
s3.discard(1) # doesn't throw error if element doesn't exist

s3.clear() # removes all elements
print(s3)


## Math Set Theory Operations, e.g.
newS= {1,2,3,4,5,6} 
otherS= {4,5}

fs= newS-otherS # filtering out unwanted elements
print(fs)




