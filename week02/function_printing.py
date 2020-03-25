def makeNegative(x):
    x *= -1
    return x

def makeNegativeAgain(x):
    x *= -1
    print(x)
    
a = makeNegative(10) + 5
b = makeNegativeAgain(15)
print(a)
print(b)