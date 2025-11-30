# Catching and reacting to different exceptions

try:
    rawInput = input("Enter the first number: ")
    a = int(rawInput)

    rawInput = input("Enter the second number: ")
    b = int(rawInput)

    result = a / b
    print(f'{a} / {b} = {result}')

except ValueError as e:
    print("Please enter valid integers")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
