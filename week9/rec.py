# Write a function that prints hello n times
# printHello(n)

def printHello(n):
    if n == 0:
        return
    else:
        print("hello")
        printHello(n-1)
    
printHello(5)
    
    