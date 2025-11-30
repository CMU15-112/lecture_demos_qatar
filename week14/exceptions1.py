def crazyFormula(x, y):
    return x/(y - 10)

try:
    print("Before crashing")
    print(crazyFormula(42, 10))
    print("This won't execute, because an exception is 'raised' in the previous call")
except:
     print("We caught an error, but we  continue")


print("We reached the end")
