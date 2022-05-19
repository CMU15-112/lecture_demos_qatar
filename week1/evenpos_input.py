# write a program that asks the user to
# input one number and then it prints
# a message if the number is even and positive


n = input("give me one number:")
n = int(n)
print("I got ", n, type(n))
isEven = (n % 2 == 0)
isPositive = (n > 0)

isEvenPos = isEven and isPositive

if isEvenPos:
    print("yey, is even and positive")

#if not isEvenPos
if isEvenPos == False:
    print("oh no")
    
print("bye")



