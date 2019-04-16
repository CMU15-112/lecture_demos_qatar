import random

def randomValue(lo, hi):
    return lo + (hi-lo)*random.random()

def randomPoint():
    x = randomValue(-1,1)
    y = randomValue(-1,1)
    return (x,y)
    
def inCircle(x,y):
    return x**2 + y**2 <= 1
    
def simulate(trials):
    insideCircle = 0
    for trial in range(trials):
        x,y = randomPoint()
        if inCircle(x,y):
            insideCircle += 1
    return 4.0 * insideCircle / trials
        