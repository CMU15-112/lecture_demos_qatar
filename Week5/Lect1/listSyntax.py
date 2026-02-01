L = [1, 2, -10, 35, 100, -3, 2] # allows duplicates
print(L)

weirdL = [1, "Hello", True, 5.2]
print(weirdL)
#print(min(weirdL))

# ordered
print([1,2,3] == [3,1,2])

### helpful functions
print("Functions ======= ")
print(len(L))
print(min(L))
print(max(L))
print(sum(L))


### Accessing elements: indexing, slicing
print("Accessing elements =======  ")
print(L[2])
print(L[-2])

print(L[::2])
print(L[::-1])

### Iterating Through Elements
print("Iterating Through Elements ======= ")
# through indicies
for i in range(len(L)):
    print(L[i])

print("---")
# through elements
for e in L:
    print(e)

### Membership
print("membership ======= ")
print( -3 in L)
print(-3 not in L)

### count
print("count ======= ")
print(L.count(2))


############### Modifying Elements (mutable)
print("Modifying Lists ============ ")

## single item
L[2] = 34
print(L)

## slice
L[2:4] = [90, 3]
print(L)

##### Add
print("Adding")

# @ END
L.append(10)
print(L)

L+=[5] #[i]
print(L)

# @ iNDEX
L.insert(2, 50)
print(L)

#### Remove
print("Removing")

# By index/slice
del L[3]
print(L)

del L[5:]
print(L)

# By Value (first occurance)
L.remove(2)
print(L)

L.append(3)
print(L)
L.remove(3)
print(L)

# last element
e = L.pop()
print(e)
print(L)

############## String <> list

print(" String <> list ======= ")

s = "Hello, World, !"

### split:  str -> list
lst = s.split(",") # list strings
print(lst)

lc = list(s) # list of chars
print(lc)

### join: list -> str
ns= "".join(lc)
print(ns)
print("-".join(lc))
print("=".join(lst))