""" I’m thinking of a number between 1 and 100.
Can you guess it?
Keep guessing until you get it right!
"""






























secretNumber = 42

guess = int(input("Guess the number (from 1 to 100):")) 
while guess != secretNumber:
    print("Try again")
    guess = int(input("Guess the number (from 1 to 100):")) 
print("You made it!" )



