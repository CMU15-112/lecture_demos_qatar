def getBalance(l):
    total=0;
    while len(l):
        total += l.pop()
    return total



savings = [100,80,125,35]

print("Aug. 30 Balance ", getBalance(savings))

savings.append(120)

print("Sept. 1 - Balance ", getBalance(savings))