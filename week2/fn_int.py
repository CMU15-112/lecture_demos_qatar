# There's no aliasing with integer arguments
def myFunction(n):
    n = 4
    return n

n = 10
print("n before calling myFunction", n)
value = myFunction(n)
print("n after calling my Function", n)