def func1():
    print("Bob ", end="")
    return False
    
def func2():
    print("eats ", end="")
    return False
    
def func3():
    print("waffles ", end="")
    return True

if func1() or (func2() and func3()):
    print("often")
else:
    print("sometimes")