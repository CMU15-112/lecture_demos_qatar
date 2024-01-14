def demoFunction(x):
    if x > 5:
        print("This is a big number!")
    else:
        print("This is a small number.")
    print("Thanks for asking")
    
demoFunction(6)
print("===")
demoFunction(4)
print("===")

def otherFunction(x,y):
    # The psychopath is probably coming for you...
    if x > 5:
        if y > 5:
            print("Both numbers are big")
        else:
            print("x is big, y is small")
    else:
        if (y > 5):
            print("y is big, x is small")
        else:
            print("Both numbers are small")

print("First call")
otherFunction(6,6)
print("Second call")
otherFunction(2,2)
print("Third call")
otherFunction(6,2)
print("Fourth call")
otherFunction(2,6)

def betterFunction(x,y):
    if x > 5 and y > 5:
        print("Both numbers are big")
    elif x > 5 and y <= 5:
        print("x is big, y is small")
    elif x <= 5 and y > 5:
        print("y is big, x is small")
    else:
        print("Both numbers are small")

