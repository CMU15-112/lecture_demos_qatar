# write myAbs(n) that returns the absolute value of n

# Print is not equal to return
def myAbsWrong(n):
    if n < 0:
        print(-n)
    else:
        print(n)

def myAbs(n):
    if n < 0:
        return -n
    # n >= 0
    return n


if myAbsWrong(-5) == 5:
    print("Yei")
else:
    print("ohno")

# This will print None: if a function doesn't return a value explicitly
# Python will return None for you
# Functions always return a value in Python, even if you don't want to
print("Abs of -5 is ", myAbsWrong(-5))

if myAbs(-5) == 5:
    print("Yei")
else:
    print("ohno")

print("Abs of -5 is ", myAbs(-5))
