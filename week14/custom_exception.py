# Writing custom exceptions

class CrazyErrorException(Exception):
    def __init__(self, message ):
        super().__init__(message)

def crazyFormula(x, y):
    if y == 10:
        raise ValueError("Please note that y can't be 10")
    return x/(y - 10)

# crazyFormula(6, 10)  # this raises an uncaught exception

try:
    print(crazyFormula(42, 10))
except CrazyErrorException:
     print("We caught a crazy error")


print("We reached the end")
