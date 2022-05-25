# x, y are integers
# x greater than y and both between 1 99, inclusive
# x != y
# right most digit of x should be equal to left most digit of y
# right most digit of y should be equal to left most digit of x
# 12, 21
# 13, 31
# 45, 54
def rc1(x, y):
    return ((type(x) == type(y) == int) and
            (100 > x > y > 0) and
            (x % 10 == y // 10) and
            (y % 10 == x // 10) and
            (x - y == 9))

#  x = 54  y = 45

#  54 45