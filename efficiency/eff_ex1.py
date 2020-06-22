# Overall: O( logN ) 
def func2(n):
    sum = 0 #  O(1)  assigning value to variable
    i = n # O(1)     copy value to variable
    while i > 0:  # Runs O( logN ) 
        sum = sum + i   # O(1) 
        i = i // 2      # O(1)
    return sum # O(1)


# n=20
# how many passes we do?
# Pass    value
# k=1    i=20    n
# k=2    i=10    n/2
# k=3    i=5     n/4
# k=4    i=2     n/8
# k=5    i=1  # THE END  5 passes


# n=40   value after
# k=1    i=40  n
# k=2    i=20  n/2
# k=3    i=10  n/4
# k=4    i=5   n/8
# k=5    i=2   n/16
# k=6    i=1   -> THE END 
