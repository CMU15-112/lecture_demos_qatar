# Assumptions:
# If the function takes a list, then N is the # items
# If the function takes an integer, then N is the integer
# If the function takes a string, then N is the # characters
# Calculate the bigOh

# O(1)
def func1(lst):
    if len(lst) > 0:  # O(1)
        return lst[0]  # O(1)
    else:
        return None  #O(1)

# O(n)
def func2(lst):
    sum = 0  # O(1)
    for i in range(len(lst)):  # O(n)
        sum += lst[i]          # O(1)
    return sum  #O(1)

# O(n)
def func3(lst):
    # Some built-ins...
    if 4 in lst:   #  O(n)
        print("hi")  # O(1)
        return True # O(1)
    return False    #O(1)

# O(n)
def func4(lst):
    # What about operating on sets?
    
    s = set(lst)   # O(n)
    if 4 in s: # O(1)
        print("hi")
        return True
    return False

# O(n**2)
def func5(lst):
    result = True
    for i in range(len(lst)): # O(n)
        for j in range(i+1, len(lst)):  # O(n)
            if lst[i] == lst[j]:
                result = False
    return result

# O(n)
def func6(lst):
    # what about dictionaries?
    d = {}  # O(1)
    for i in lst: # O(n)
        c = d.get(i, 0)  # O( 1)
        d[i] = c+1  # O(1)
    return d
