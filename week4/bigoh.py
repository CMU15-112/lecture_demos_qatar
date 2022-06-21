# O(1)
def func1(lst):
    if len(lst) > 0:
        return lst[0]
    else:
        return None
# O(n)
def func2(lst):  # n 
    sum = 0
    for i in range(len(lst)): # n it: O(n)
        sum += lst[i]  # O(1)
    return sum

# O(n)
def func3(lst):
    # Some built-ins...
    if 4 in lst: # O(n)
        if 5 in lst: #O(n)
            print("hi")
            return True
    return False