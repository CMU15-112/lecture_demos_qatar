t = (1,2,3)
print(type(t), t)

### list > tuple
L = [4,5,6]
t2 = tuple(L)
print(t2)

## Accessing elements
print(t[1])
print(t[-1])
print(t[:2])


## Modifying
#t[1] = 42 # immutable
print(t)

### ordered
print((1,2,3) == (1,3,2))

print(len(t))