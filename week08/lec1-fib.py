def fib(n, depth=0):
    print("  "*depth + "fib("+str(n)+")")
    # Base case
    if n == 1:
        ret = 0
    elif n == 2:
        ret = 1
    else:
        # recursive case
        ret = fib(n-1, depth+1) + fib(n-2, depth+1)
    
    print("  "*depth + "--> " + str(ret))
    return ret

print("final",fib(7))