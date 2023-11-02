# Assumptions:
# If the function takes a list, then N is the # items
# If the function takes an integer, then N is the integer
# If the function takes a string, then N is the # characters

def func1(lst):
    if len(lst) > 0:
        return lst[0]
    else:
        return None

def func2(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

def func3(lst):
    # Some built-ins...
    if 4 in lst:
        print("hi")
        return True
    return False

def func4(lst):
    # What about operating on sets?
    s = set(lst)
    if 4 in s:
        print("hi")
        return True
    return False

def func5(lst):
    result = True
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                result = False
    return result

def func6(lst):
    # what about dictionaries?
    d = {}
    for i in lst:
        c = d.get(i, 0)
        d[i] = c+1
    return d
