def absoluteValue(x):
    if x < 0:
        x = -x
    else:
        x = x
    print("abs = ", x)  # print is not return!

number = -5

crazyformula = absoluteValue(number)**number

absValue = absoluteValue(number) # Error, absoluteValue(number) is not returning a number

print(absValue)
print(type(absValue))

def absoluteValueOK(x):
    if x < 0:
        x = -x
    else:
        x = x
    return x
