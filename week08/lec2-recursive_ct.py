def ct1(n, depth=0):
    print("Depth " + str(depth) + " input: " + str(n))
    result = None
    if n <= 2:
        result = 1
    elif n % 2 != 0:
        result = 1 + ct1(n - 1, depth+1)
    else:
        result = 2 + ct1(n // 2, depth+1)
    print("Depth " + str(depth) + " output: " + str(result))
    return result

ct1(6)