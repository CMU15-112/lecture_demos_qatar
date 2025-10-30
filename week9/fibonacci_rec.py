def fibonacci_rec(n):

    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    
print(fibonacci_rec(5))