import math

# Assumptions:
# If the function takes a list, then N is the # items
# If the function takes an integer, then N is the integer
# If the function takes a string, then N is the # characters

# O(1)
def func1(lst):
    if len(lst) > 0:
        return lst[0]
    else:
        return None

# O(log N)
def func2(n):
    sum = 0
    i = n
    while i > 0: # 
        sum = sum + i
        i = i // 2
    return sum

# O(N^0.5) or O(sqrt(N))
def func3(lst):
    num = len(lst)
    if num < 2: 
        return False
    result = True
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            result = False
    return result

# O(N)
def func4(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

# O(N log N)
def func5(lst):
    n = len(lst) 
    result = None
    for i in range(len(lst)):
        num = n
        while num > 0:
            if lst[i] == num: 
                result = lst[i]
            num = num // 2
    return result

# O(N^2)
def func6(lst):
    result = True
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                result = False
    return result
