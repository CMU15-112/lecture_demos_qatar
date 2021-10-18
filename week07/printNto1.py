def printNto1(n):
    if n == 0:
        return 
    print(n)
    n = n-1
    printNto1(n)
    
printNto1(5)