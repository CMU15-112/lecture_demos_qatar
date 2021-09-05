def secretNumber():
    return 42

def secretFunction(x):
    x += secretNumber()
    return x

print("double of 8 is ", doubleNumber(8))
    

newNumber = secretFunction(1)

print(newNumber)
