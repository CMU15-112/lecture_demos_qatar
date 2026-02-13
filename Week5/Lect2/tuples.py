# CREATING TUPLE
t = (1, 2, 3)
print(type(t), len(t), t)

# FROM LIST TO TUPLE
a = [1, 2, 3]
t = tuple(a)
print(type(t), len(t), t)

# ACCESSING ELEMENTS - INDEXING AND SLICING
t = (1, 2, 3)
print(t[0])
print(t[1:])

### can iterate the same way as lists

# MODIFYING
#t[0] = 42    # crash! tupes are immutable
print(t[0])

# Orderted
print((1,2,3)==(3,1,2))