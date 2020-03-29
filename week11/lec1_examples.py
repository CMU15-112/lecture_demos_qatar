import math

# Assumptions:
# If the function takes a list, then N is the # items
# If the function takes an intenger, then N is the integer
# If the function takes a string, then N is the # characters

# Overall: O(1)
# Constant time
def func1(lst):
    if len(lst) > 0: # O(1)
        return lst[0] # O(1)
    else: # O(1)
        return None # O(1)

# Overall: O(log N)
# Logarithmic
def func2(n):
    sum = 0 # O(1)
    i = n # O(1)
    while i > 0:  # Runs O(log N) times
        sum = sum + i # O(1)
        i = i // 2 # O(1)
    return sum # O(1)

# Overall: O(sqrt N)
def func3(lst):
    num = len(lst) # O(1)
    if num < 2:  # O(1)
        return False # O(1)
    result = True # O(1)
    for i in range(2, int(math.sqrt(num))): # Runs O(sqrt(N)) times
        if num % i == 0: # O(1)
            result = False # O(1)
    return result # O(1)

# O(N)
# Linear
def func4(lst):
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

# O(N log N)
# Linearithmic
def func5(lst):
    n = len(lst)  # O(1)
    result = None # O(1)
    for i in range(len(lst)): # Runs O(N) times
        num = n # O(1)
        while num > 0: # Runs O(log N) times
            if lst[i] == num:  # O(1)
                result = lst[i] # O(1)
            num = num // 2 # O(1)
    return result # O(1)

# O(N^2)
# Quadratic
def func6(lst):
    result = True # O(1)
    for i in range(len(lst)): # Runs N times
        for j in range(i+1, len(lst)): # Runs N times
            if lst[i] == lst[j]: # O(1)
                result = False # O(1)
    return result # O(1)