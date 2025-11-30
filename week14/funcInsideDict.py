from math import sin, cos
def cube(x):
    return x**3
def square(x):
    return x * x

funcs = {
    "x-square": square,
    "x-cube":   cube,
    "sin":    sin,
    "cos":    cos
}

choice = input(f'Pick one function: {funcs.keys()}')
if choice not in funcs:
    print("not available")
else:
    value = float(input(f'enter a number'))
    print(f'The derivative of {choice} @ {value} is {derivative(funcs[choice], value)}')
    