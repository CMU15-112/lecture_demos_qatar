
### Creating sets

# from string
s= set("Hello")
print(s)

#statically allocated
s= {1,2,3,3,"A", "B"}
print(s)

#empty set
s= set()
print(s)

#{} is a dictionary
print(type({}))


### element properties: unique, unordered, and immutable

# unordered

L1= [1,2,3,4]
L2=[1,3,2,4]

print("L1==L2?", L1==L2)

s1= set(L1)
s2= set(L2)

print("s1==s2", s1==s2)

#print(s1[0])

# immutable
s= {1, "Hello", (3,4), False}# [1,2]
print(s)



### Iterating over the elmenets

for e in s:
    print(e)
    
### membership    

print("membership")
print(3 in s)
print(False not in s)
print((3,4) in s)

##Adding elements

s.add("A")

s.update([5,6])
s.update({"World"})

print(s)

# Removing elements

s.remove(1)
print(s)

#s.remove(3) 
#print(s)

s.discard(3)
print(s)

s.clear()

