import copy

def func1(n):
    for x in range(0, 2**n, 2**n//n**2):
        print("This may print a lot!")

def func2(n):
    x = 0    

    while (x < n):
        y = 0 
        while (y < n):
            print("y")
            y += 1
        print("x")
        x += 1

def func3(n):
    x = 0
    y = 0 

    while (x < n):
        while (y < n):
            print("y")
            y += 1
        print("x")
        x += 1

def func4(n):
    for x in range(n):
        for y in range(n):
            print(x,y)
    for x in range(n):
        print("huzzah!")


def func5(n):
    for x in range(n):
        for y in range(100):
            print(x,y)
    for x in range(n):
        print("huzzah!")
 
def func6(n):
    x = int(round(n**0.5))
    for x in range(1, x):
        print("Go team!")

def func7(n):
    step = int(round(n**0.5))
    for x in range(1, n**2, step):
        print("Go team!")

def func8(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return None

def func9(lst):
    tmp = copy.copy(lst)
    
    for i in range(len(lst)):
        j = 1
        while j < len(lst):
            j *= 2 
        lst[i] = j
    print(tmp, lst)
    
def func10(s):
    for c in s:
        for t in "aeiou":
            if c == t:
                return False
    return True