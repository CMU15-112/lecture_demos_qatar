def myFunc1(someList):
    someList[-1] = 0

def myFunc2(someInt):
    someInt = 0
    
theList = [1, 2, 3, 4]
theInt = 10

myFunc1(theList)
myFunc2(theInt)

print(theList)
print(theInt)