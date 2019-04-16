import random

def tryBirthdayMatch(numPeople):
    bdayList = []
    for i in range(numPeople):
        bday = random.randint(1,365)
        bdayList.append(bday)
    return len(bdayList) != len(set(bdayList))
    
def simulate(numPeople, trials=10**5):
    success = 0
    for i in range(trials):
        if tryBirthdayMatch(numPeople) == True:
            success += 1
    return success/trials
    
for i in range(50):
    print(i, simulate(i))