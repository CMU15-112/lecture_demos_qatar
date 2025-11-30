x = 42
y = 67.0
z = 'hello'
print(x)
print(x, y)
print(x, y, z)
print(x, y, z, sep = ' -- ')
print(x, y, z, x, y, y, sep = ' -- ', end = '****THE END****\n')

def myFlexibleFunction(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)
    boring = kwargs.get('boring', False)
    if not boring:
        print("I'm glad you are not bored")
    else:
        print(":(")

myFlexibleFunction(10, 20, name="Eduardo", active=True, boring=True)