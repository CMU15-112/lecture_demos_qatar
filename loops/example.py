# now, ask the user for n inputs (numbers) and at the end, compute the sum, and print total = xxx

# step 1: ask how many numbers
n = int( input("how many numbers do you want to sum?") )

# step 2--:
thesum=0
for i in range(n):
    theinput = input("give me a number")
    if theinput.isdigit():  # it is a number
        thenumber = int(theinput)
        thesum = thesum + thenumber 
        print("number",i+1,"=",thenumber)
    else:
        print("Invalid input, try again")
        

print("The sum is ", thesum)
