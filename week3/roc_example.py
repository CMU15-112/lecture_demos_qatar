# Find values for x and y such that the function returns True

# x, y are integers
# x greater than y and both between 1 99, inclusive
# right most digit of x should be equal to left most digit of y
# right most digit of y should be equal to left most digit of x
# diff between x and y is 9

# lets try some
# x=32  y=23

def rc1(x, y):
    return ((type(x) == type(y) == int) and
            (100 > x > y > 0) and
            (x % 10 == y // 10) and
            (y % 10 == x // 10) and
            (x - y == 9))

print(rc1(32,23))
print(rc1(10,1))




