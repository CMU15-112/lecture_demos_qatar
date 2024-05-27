import copy

a= [1,2,3,4]
b= a # alias

print(f"a @ {id(a)}")
print(f"b @ {id(b)}")

# Ctreate a copy
c = []
for e in a:
    c.append(e)
print(c)
print(f"c @ {id(c)}")

d= a[:]
print(d)
print(f"d @ {id(d)}")

e= copy.copy(a)
print(e)
print(f"e @ {id(e)}")



# comparing the values (==)
print("a==b: ", a==b)
print("a==c: ", a==c)

# comparing objects or comparing whether they refer to the same thing in memory (is)
print("a is b: ", a is b)
print("a is c: ", a is c)

a[0] = 6
print("After modifying a -----")
# comparing the values (==)
print("a==b: ", a==b)
print("a==c: ", a==c)

# comparing objects or comparing whether they refer to the same thing in memory (is)
print("a is b: ", a is b)
print("a is c: ", a is c)

# function parameters are aliases
def f(b):
    b+=[4]   
    print(f"Inside f: b @ {id(b)}")
    
a= [1,2,3]
print(f"B4 f: a @ {id(a)}")
f(a)
print(a)

