# Write a function to print multiple of 2s between to given
# values a and b (inclusive) in one line
# printMultipleOf2s(1, 10):
# I should see:
# 2 4 6 8 10

"""
def printMultipleOf2s(a, b):
    # for i in range(start, end, step)
    for i in range(a, b+1):
        if i % 2 == 0:
            print(i, end=" ")
"""
    
def printMultipleOf2s(a, b):
    # for i in range(start, end, step)
    if a%2 == 1:
        a = a + 1
    for i in range(a, b+1, 2):
        print(i, end=" ")
        
printMultipleOf2s(1, 12)
    