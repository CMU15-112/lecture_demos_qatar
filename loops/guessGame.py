chances = 5
secret_number = 87
while chances > 0:        
    x = int(input("Try to guess a secret number between 0 and 112, make a guess"))
    if x < secret_number:
        print("Too low, try again")
    elif x > secret_number:
        print("Too high, try again")
    else:
        print("You guessed right! conratulations")
        break
    chances -= 1
    