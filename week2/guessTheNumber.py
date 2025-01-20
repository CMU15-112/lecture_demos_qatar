import random
secretNumber = random.randint(1, 10)

guess = int(input("guess the number:")) 
while guess != secretNumber:
    print("Try again")
    guess = int(input("guess the number:")) 
print("You made it!" )