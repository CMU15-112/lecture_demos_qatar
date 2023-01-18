# Write the function printNFibonacci that takes a positive integer n 
# and prints the first n Fibonacci numbers

def printNFibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b , a+b
        
printNFibonacci(7)
        
        