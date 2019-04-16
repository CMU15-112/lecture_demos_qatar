import random

def rollDie():
    return random.randint(1,6)
    
def rollDice(numDice):
    sum = 0
    for i in range(numDice):
        sum += rollDie()
    return sum
    
def simulate(numDice, trials=100):
    
    rollHistory = dict()
    for i in range(trials):
        roll = rollDice(numDice)
        
        if roll in rollHistory:
            rollHistory[roll] += 1
        else:
            rollHistory[roll] = 1
            
    for i in range(0, 6*numDice+1):
        if i in rollHistory:
            print(i,rollHistory[i])
        else:
            print(i, 0)
        