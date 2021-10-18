cache = {}
def fib(n, depth=0):
    if n in cache:
        return cache[n]
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
    cache[n] = ret
    return ret

print("final",fib(20))
