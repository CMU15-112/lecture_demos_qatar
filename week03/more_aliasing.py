def myFunc1(a):
    print("a:", a)
    a = 5

x = 6
myFunc1(x)
print("x:",x)

print("------")

def myFunc2(myList):
    print("myList:", myList)
    myList[0] = 10
    
L = [1,2,3,4]
myFunc2(L)
print(L)